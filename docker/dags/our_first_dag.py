from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Moises',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id="dag_teste",
    default_args=default_args,
    description="Nossa primeira Dag",
    start_date=datetime(2025, 5, 14, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='dag_teste',
        bash_command="echo hello world, primeira task!"
    )

    task1
