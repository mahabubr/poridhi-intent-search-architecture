from fastapi import FastAPI
from dotenv import load_dotenv

from app.router import intent_search

load_dotenv()

from .qdrant import qdrant_client

qdrant_client.get_client()

app = FastAPI()

app.include_router(intent_search.router)


@app.get("/")
def product_intent_search_architecture():
    return {
        "success": True,
        "message": "Welcome To Product Intent Search Architecture System",
    }
