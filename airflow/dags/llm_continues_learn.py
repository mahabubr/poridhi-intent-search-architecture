from airflow import DAG
from datetime import datetime
from airflow.providers.standard.operators.python import PythonOperator


def extract_data_callable():
    print("Extracting data from an weather API")


with DAG(
    dag_id="llm_continues_learn",
    start_date=datetime(year=2025, month=1, day=1, hour=0, minute=0),
    schedule="@daily",
    catchup=True,
    max_active_runs=1,
    render_template_as_native_obj=True,
) as dag:

    extract_data = PythonOperator(
        dag=dag, task_id="extract_data", python_callable=extract_data_callable
    )

    extract_data
