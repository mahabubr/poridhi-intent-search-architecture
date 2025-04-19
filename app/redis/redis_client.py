import redis.asyncio as redis
from app.config.dotenv import REDIS_CACHE_HOST, REDIS_CACHE_PORT


redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
