from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
)
from datasets import Dataset
import os
import time
import glob

base_dir = os.path.dirname(os.path.abspath(__file__))

BASE_VAULT_PATH = os.path.join(base_dir, "../fine_tune_vault")

MODEL_BASE_NAME = "flan-t5-query-refiner"


def get_latest_version_path():
    version_dirs = glob.glob(os.path.join(BASE_VAULT_PATH, f"{MODEL_BASE_NAME}-v*"))
    versions = [
        int(d.split("-v")[-1]) for d in version_dirs if d.split("-v")[-1].isdigit()
    ]
    return max(versions) if versions else 0


def get_next_version_path():
    """Generate new version directory path"""
    return os.path.join(
        BASE_VAULT_PATH, f"{MODEL_BASE_NAME}-v{get_latest_version_path() + 1}"
    )


def llm_learn():
    CSV_PATH = "dataset/web_search_tune.csv"

    if not os.path.exists(CSV_PATH) or os.stat(CSV_PATH).st_size == 0:
        return

    try:
        df = pd.read_csv(CSV_PATH)
        if df.empty or not {"query", "answers"}.issubset(df.columns):
            print("No Data Found For Training...")
            return

        new_version_path = get_next_version_path()
        os.makedirs(new_version_path, exist_ok=True)

        latest_version = get_latest_version_path()
        base_model_path = os.path.join(
            BASE_VAULT_PATH,
            (
                f"{MODEL_BASE_NAME}-v{latest_version}"
                if latest_version > 0
                else MODEL_BASE_NAME
            ),
        )

        model = AutoModelForSeq2SeqLM.from_pretrained(base_model_path)
        tokenizer = AutoTokenizer.from_pretrained(base_model_path)

        hf_dataset = Dataset.from_pandas(df)

        def tokenize_function(examples):
            inputs = tokenizer(
                examples["query"], max_length=512, truncation=True, padding="max_length"
            )
            with tokenizer.as_target_tokenizer():
                labels = tokenizer(
                    examples["answers"],
                    max_length=512,
                    truncation=True,
                    padding="max_length",
                )
            inputs["labels"] = labels["input_ids"]
            return inputs

        tokenized_dataset = hf_dataset.map(tokenize_function, batched=True)

        training_args = Seq2SeqTrainingArguments(
            output_dir=new_version_path,
            num_train_epochs=1,
            per_device_train_batch_size=4,
            learning_rate=1e-5,
            save_strategy="no",
            logging_steps=50,
            report_to="none",
            disable_tqdm=True,
        )

        trainer = Seq2SeqTrainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_dataset,
        )

        trainer.train()

        model.save_pretrained(new_version_path)
        tokenizer.save_pretrained(new_version_path)
        training_args.save_to_json(os.path.join(new_version_path, "training_args.json"))

        pd.DataFrame().to_csv(CSV_PATH, index=False)
        print(f"Created new model version at {new_version_path}")

    except Exception as e:
        print(f"Training error: {str(e)}")


scheduler = BackgroundScheduler()

scheduler.add_job(llm_learn, "interval", minutes=1)


def start_model_continues_learn():
    scheduler.start()


def shutdown_model_continues_learn():
    scheduler.shutdown()
