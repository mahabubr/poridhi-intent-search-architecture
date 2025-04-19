from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"


class RefineQueryModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    def process(self, raw_text: str):
        instruction = f"Rewrite this to be more concise and optimized for search engine input: {raw_text}"

        inputs = self.tokenizer(
            instruction,
            return_tensors="pt",
        )

        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=64,
            num_beams=5,
            no_repeat_ngram_size=2,
            early_stopping=True,
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()


refine_query_model = RefineQueryModel()
