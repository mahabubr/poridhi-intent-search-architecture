from logger.query_logger import refine_query_logger
import time
from app.model_vault.refine_query_model import refine_query_model


def query_manager(search):
    start_time = time.time()

    refine_search = refine_query_model(search)

    execution_time = time.time() - start_time

    refine_query_logger(
        search=search, refine_search=refine_search, execution_time=execution_time
    )

    return refine_search
