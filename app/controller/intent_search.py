from app.service.intent_search import intent_search as intent_search_service


def intent_search():
    response = intent_search_service()

    return response
