import logging
import os

filename = os.path.join(os.getcwd(), "logger", "logs", "query_refine.log")

# Create logger
refine_logger = logging.getLogger("refine_query")
refine_logger.setLevel(logging.INFO)

# Avoid adding handlers multiple times
if not refine_logger.handlers:
    file_handler = logging.FileHandler(filename)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    refine_logger.addHandler(file_handler)


def refine_query_logger(search, refine_search, execution_time):
    refine_logger.info("=" * 75)
    refine_logger.info("  Intent Search Process Initiated  ")
    refine_logger.info("=" * 75)

    refine_logger.info("  Search Query: %s", search)
    refine_logger.info("  Refined Search Query: %s", refine_search)
    refine_logger.info("  Execution Time: %.4f seconds", execution_time)

    refine_logger.info("=" * 75)
    refine_logger.info("  Intent Search Process Completed ")
    refine_logger.info("=" * 75 + "\n")
