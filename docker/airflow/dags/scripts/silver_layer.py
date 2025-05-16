from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from datetime import datetime
from minio import Minio
import pandas as pd
import io
import json

def processa_dados_silver_layer():
    # 1. Conecta no MinIO
    minio_client = Minio(
        endpoint="minio:9000",
        access_key="datalake",
        secret_key="datalake",
        secure=False
    )

    # 2. Lê o arquivo JSON da camada bronze
    today = datetime.now().strftime("%Y-%m-%d")
    bucket = "bronze-layer"
    file_name = f"breweries_raw_{today}.json"
    
    response = minio_client.get_object(bucket, file_name)
    json_data = json.load(io.BytesIO(response.read()))

    # 3. Cria um Pandas DataFrame
    pandas_df = pd.DataFrame(json_data)

    # 4. Inicializa Spark
    spark = SparkSession.builder \
        .appName("BrewerySilverETL") \
        .getOrCreate()

    # 5. Converte para Spark DataFrame
    df = spark.createDataFrame(pandas_df)

    # 6. Transformações e limpeza
    silver_df = df.select(
        col("id"),
        col("name"),
        col("brewery_type"),
        col("street"),
        col("city"),
        col("state"),
        col("postal_code"),
        col("country"),
        col("longitude").cast("double").alias("longitude"),
        col("latitude").cast("double").alias("latitude"),
        col("phone"),
        col("website_url")
    ).withColumn("state", when(col("state").isNull(), "UNKNOWN").otherwise(col("state")))

    # 7. Salva na camada silver com particionamento
    silver_path = "s3a://brewery-silver/breweries"
    silver_df.write.mode("overwrite").partitionBy("state").parquet(silver_path)

    spark.stop()
    print(f"Processamento concluído e dados salvos em {silver_path}")
