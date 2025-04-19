from transformers import pipeline
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

model_dir = os.path.join(base_dir, "../fine_tune_vault/flan-t5-query-refiner-model")
tokenizer_dir = os.path.join(base_dir, "../fine_tune_vault/flan-t5-query-refiner-token")

model_dir = os.path.abspath(model_dir)
tokenizer_dir = os.path.abspath(tokenizer_dir)


def refine_query_model(raw_query):
    refiner = pipeline(
        "text2text-generation",
        model=model_dir,
        tokenizer=tokenizer_dir,
    )

    refined_query = refiner(
        f"refine e-commerce query: {raw_query}",
        max_length=128,
        num_beams=8,
        early_stopping=True,
    )

    query = refined_query[0]["generated_text"]

    return query
