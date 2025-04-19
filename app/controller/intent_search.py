from app.service.intent_search import intent_search as intent_search_service


async def intent_search(search):
    response = await intent_search_service(search)

    return response
