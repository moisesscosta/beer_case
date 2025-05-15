from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from datetime import datetime
import os


def processa_dados_silver_layer():
    # Configuração do Spark
    spark = SparkSession.builder \
        .appName("BrewerySilverETL") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk-bundle:1.11.901") \
        .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
        .config("spark.hadoop.fs.s3a.access.key", os.getenv("MINIO_ACCESS_KEY")) \
        .config("spark.hadoop.fs.s3a.secret.key", os.getenv("MINIO_SECRET_KEY")) \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()

    # Data atual para pegar o arquivo correto
    today = datetime.now().strftime("%Y-%m-%d")
    bronze_path = f"s3a://brewery-bronze/breweries_raw_{today}.json"

    # Lê os dados bronze
    df = spark.read.json(bronze_path)

    # Seleciona e transforma colunas
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

    # Escreve na camada silver particionado por estado
    silver_path = "s3a://brewery-silver/breweries"
    silver_df.write.mode("overwrite").partitionBy("state").parquet(silver_path)

    spark.stop()
