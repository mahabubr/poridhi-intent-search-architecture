from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def call_fastapi_endpoint():
    print("Call From DAG --> ENDPOINT")


with DAG(
    "fastapi_integration",
    default_args=default_args,
    schedule=timedelta(minutes=2),
    catchup=False,
) as dag:

    call_api_task = PythonOperator(
        task_id="call_fastapi_endpoint",
        python_callable=call_fastapi_endpoint,
    )
