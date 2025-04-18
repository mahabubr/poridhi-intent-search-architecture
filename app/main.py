from fastapi import FastAPI
from dotenv import load_dotenv

from app.router import intent_search

load_dotenv()

app = FastAPI()

app.include_router(intent_search.router)


@app.get("/")
def product_intent_search_architecture():
    return {
        "success": True,
        "message": "Welcome To Product Intent Search Architecture System",
    }
