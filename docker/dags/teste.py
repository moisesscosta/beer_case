
import sys
import os  # <- Adicione isso aqui

from scripts.bronze_layer import carrega_dados_raw_bucket_s3
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Para importar scripts fora do diretório atual
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
