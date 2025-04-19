from app.manager.refine_query_manager import query_manager
from app.manager.search_cache_manager import get_search_cache, set_search_cache
from app.model_vault.embedding_model import EmbeddingModel
from app.qdrant.qdrant_service import search_qdrant
from app.manager.fetch_product_manager import fetch_product

model_name = "sentence-transformers/all-MiniLM-L6-v2"


async def intent_search(search):
    refine_query = query_manager(search=search)

    exist_cache = await get_search_cache(refine_query)

    if exist_cache:
        return {
            "success": True,
            "message": "Product retrieve successful",
            "data": exist_cache,
        }

    embedding_model = EmbeddingModel(model_name)

    embedding = embedding_model.embed(refine_query)

    vector_db = search_qdrant(embedding, 10)

    product_ids = [point.payload["uniq_id"] for point in vector_db]

    products = fetch_product(product_ids)

    await set_search_cache(refine_query, products)

    return {
        "success": True,
        "message": "Product retrieve successful",
        "data": products,
    }
