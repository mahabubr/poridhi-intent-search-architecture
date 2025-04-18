from sentence_transformers import SentenceTransformer
from typing import List, Union


class EmbeddingModel:
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed(
        self, text: Union[str, List[str]]
    ) -> Union[List[float], List[List[float]]]:
        if isinstance(text, str):
            embedding = self.model.encode(
                text,
                normalize_embeddings=True,
                batch_size=32,
                show_progress_bar=True,
            )
            return embedding.tolist()
        elif isinstance(text, list):
            embeddings = self.model.encode(
                text,
                normalize_embeddings=True,
                batch_size=32,
                show_progress_bar=True,
            )
            return [e.tolist() for e in embeddings]
        else:
            raise ValueError("Input must be a string or a list of strings.")
