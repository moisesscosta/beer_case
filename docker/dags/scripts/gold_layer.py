from pyspark.sql import SparkSession
from pyspark.sql.functions import count
from datetime import datetime
import os


def agrega_dados_gold_layer():
    # Configuração do Spark
    spark = SparkSession.builder \
        .appName("BreweryGoldETL") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk-bundle:1.11.901") \
        .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
        .config("spark.hadoop.fs.s3a.access.key", os.getenv("MINIO_ACCESS_KEY")) \
        .config("spark.hadoop.fs.s3a.secret.key", os.getenv("MINIO_SECRET_KEY")) \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()

    # Lê os dados da camada silver
    silver_path = "s3a://brewery-silver/breweries"
    df = spark.read.parquet(silver_path)

    # Cria agregações
    gold_df = df.groupBy("brewery_type", "state", "country") \
        .agg(count("*").alias("brewery_count")) \
        .orderBy("country", "state", "brewery_type")

    # Escreve na camada gold
    gold_path = "s3a://brewery-gold/breweries_aggregated"
    gold_df.write.mode("overwrite").parquet(gold_path)

    # Salva também como tabela temporária para uso no PostgreSQL
    gold_df.createOrReplaceTempView("brewery_aggregates")

    spark.stop()
