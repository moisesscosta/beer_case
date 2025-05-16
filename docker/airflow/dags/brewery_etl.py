import sys
import os

#from scripts.gold_layer import agrega_dados_gold_layer
from scripts.silver_layer import processa_dados_silver_layer
from scripts.bronze_layer import carrega_dados_raw_bucket_s3
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator  # type: ignore
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'brewery_data_pipeline',
    default_args=default_args,
    description='Pipeline para processamento de dados de cervejarias',
    schedule_interval='@daily',
    start_date=datetime(2025, 5, 15),
    catchup=False,
    tags=['brewery', 'data_lake'],
)

bronze_task = PythonOperator(
    task_id='carrega_dados_raw_bucket_s3',
    python_callable=carrega_dados_raw_bucket_s3,
    dag=dag
)

# Task para a camada Silver
silver_task = PythonOperator(
    task_id='processa_dados_silver_layer',
    python_callable=processa_dados_silver_layer,
    dag=dag
)

## Task para a camada Gold
#gold_task = PythonOperator(
#    task_id='agrega_dados_gold_layer',
#    python_callable=agrega_dados_gold_layer,
#    dag=dag
#)

# Definindo a ordem de execução
bronze_task >> silver_task 
# >> gold_task
