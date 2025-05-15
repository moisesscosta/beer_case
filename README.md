## Objetive
Demonstrate with a architecture, the knowledge about de ecossystem, since the beggining with:
1. Conecction with API;
2. Data Transformation;
3. Data Orchestration;
4. Processing Layer;
5. Monitoring and Alert process

## Archtecture
1. Docker as a infrastructure
   a. Airflow as a Orchestrator
   b. MinIO as S3
   c. Spark as processor layer
2. Medallion Archtecture
   a. Bronze-Layer as a layer with raw data.
   b. Silver-Layer as a processed data, with a columnar storage format in parquet file. 
   c. Gold-Layer as a layer with data for the business

### Monitoring/Alerting
Li alguns artigos, para conhecer mais das ferramentas de observabilidade, uma que gostei foi o grafana. O Grafana me possbilitaria  criar o que chamam de  "traces", onde eu poderia enviar ao grafana possibilidade de que ele me gere métricas que podem me indicar um gargalo, um processamento muito alto.
Grafana Também permite que alem das métricas, me gere logs do que foi executado, possibilitando que eu crie alertas e possa disparar esses alertas para times, pessoas em específico, a fim de dar possibilidade do time entrar com uma correção.
