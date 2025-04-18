from fastapi import APIRouter
from app.controller.intent_search import intent_search as intent_search_controller


router = APIRouter(prefix="/intent-search", tags=["intent-search"])


@router.get("")
def intent_search():
    response = intent_search_controller()

    return response
