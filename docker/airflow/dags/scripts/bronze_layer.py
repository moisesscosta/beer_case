import requests
import pandas as pd
import json
from datetime import datetime
from minio import Minio
import io  # Adicione isso


def carrega_dados_raw_bucket_s3():
    # Configurações do Minio
    minio_client = Minio(
        endpoint="minio:9000",  # Use o nome do container no docker-compose
        access_key="datalake",
        secret_key="datalake",
        secure=False
    )

    bucket_name = "bronze-layer"
    today = datetime.now().strftime("%Y-%m-%d")
    file_name = f"breweries_raw_{today}.json"

    # Verifica se o bucket existe, se não, cria
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)

    # Coleta dados da API
    url = "https://api.openbrewerydb.org/v1/breweries"
    all_breweries = []
    n = 1

    while True:
        params = {'per_page': 50, 'page': n}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            breweries = response.json()

            if len(breweries) > 0:
                all_breweries.extend(breweries)
                n += 1
            else:
                break
        except requests.exceptions.RequestException as e:
            print(f"Erro na página {n}: {e}")
            break

    # Salva no MinIO
    json_data = json.dumps(all_breweries).encode("utf-8")  # Encode para bytes
    json_buffer = io.BytesIO(json_data)  # Arquivo em memória

    minio_client.put_object(
        bucket_name=bucket_name,
        object_name=file_name,
        data=json_buffer,
        length=len(json_data),
        content_type="application/json"
    )

    print(f"Saved {len(all_breweries)} breweries to {bucket_name}/{file_name}")
