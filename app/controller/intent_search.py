from app.service.intent_search import intent_search as intent_search_service


def intent_search(search):
    response = intent_search_service(search)

    return response
