import hashlib
import json
from app.redis.redis_client import redis_client


def sha256_key(raw_key: str) -> str:
    return hashlib.sha256(raw_key.encode()).hexdigest()


def to_dict(model):
    return {
        column.name: getattr(model, column.name) for column in model.__table__.columns
    }


def list_to_dicts(model_list):
    return [to_dict(model) for model in model_list]


async def get_search_cache(search: str):
    key = sha256_key(search)

    value = await redis_client.get(key)

    if value is None:
        return False

    return json.loads(value)


async def set_search_cache(search, value):
    key = sha256_key(search)

    value = json.dumps(list_to_dicts(value))

    await redis_client.set(key, value, ex=300)
