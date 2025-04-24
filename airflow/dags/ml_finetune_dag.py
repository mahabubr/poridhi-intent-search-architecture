from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time


def fine_tune_model():
    print("Starting ML fine-tuning job...")
    time.sleep(10)
    print("Fine-tuning complete.")


with DAG(
    dag_id="ml_finetune_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="* * * * *",
    catchup=False,
) as dag:
    fine_tune = PythonOperator(
        task_id="fine_tune_model",
        python_callable=fine_tune_model,
    )
