from qdrant_client import QdrantClient
from app.config.dotenv import QDRANT_HOST, QDRANT_PORT


qdrant = QdrantClient(host=QDRANT_HOST, port=int(QDRANT_PORT), timeout=10000.0)


def get_client():
    print(qdrant.get_collections())

    return qdrant
