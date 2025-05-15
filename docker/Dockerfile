FROM apache/airflow:2.6.0-python3.10

USER airflow

# Evita problemas com cache e dependências antigas
RUN pip install --no-cache-dir \
    pyspark==3.3.2 \
    minio==7.1.15 \
    pandas \
    boto3
USER airflow
