from app.manager.refine_query_manager import query_manager


def intent_search(search):
    refine_query = query_manager(search=search)

    return {"message": "Let's Deep Drive"}
