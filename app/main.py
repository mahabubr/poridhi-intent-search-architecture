from fastapi import FastAPI
from app.router import intent_search

app = FastAPI()

app.include_router(intent_search.router)


@app.get("/")
def product_intent_search_architecture():
    return {
        "success": True,
        "message": "Welcome To Product Intent Search Architecture System",
    }
