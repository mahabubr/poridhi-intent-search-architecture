def get_score_stats(vector_db):
    scores = [point.score for point in vector_db]

    return {"min": min(scores), "max": max(scores), "avg": sum(scores) / len(scores)}
