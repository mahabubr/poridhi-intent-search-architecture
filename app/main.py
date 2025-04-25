from fastapi import FastAPI
from dotenv import load_dotenv

from .schedular.llm_continues_learn import (
    start_model_continues_learn,
    shutdown_model_continues_learn,
)

from app.router import intent_search

load_dotenv()

from .qdrant import qdrant_client

qdrant_client.get_client()

app = FastAPI()

app.include_router(intent_search.router)


@app.on_event("startup")
async def startup():
    print("FastAPI app is starting...")

    start_model_continues_learn()


@app.on_event("shutdown")
async def shutdown():
    print("FastAPI app is shutting down...")

    shutdown_model_continues_learn()


@app.get("/")
def product_intent_search_architecture():
    return {
        "success": True,
        "message": "Welcome To Product Intent Search Architecture System",
    }
