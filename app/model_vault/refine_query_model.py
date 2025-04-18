from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-large"


class RefineQueryModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    def process(self, raw_text: str):
        instruction = "Refine this search query to make it more specific, concise, and clear, while keeping its meaning intact. "

        prompt = f"{instruction} {raw_text}"

        inputs = self.tokenizer(prompt, return_tensors="pt")

        outputs = self.model.generate(
            inputs["input_ids"],
        )

        return self.tokenizer.decode(outputs[0], skip_special_token=True)


refine_query_model = RefineQueryModel()
