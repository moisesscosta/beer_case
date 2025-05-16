# Apresentação
Demonstrar a arquitetura do tipo "medallion", com camadas de dados brutos(bronze layer), camada de dados processados(silver layer) e a camada de dados agregados(gold layer).

### Arquitetura
Usei um docker para compor os componentes de que preciso
Contem:
   1. Minio - Storage
   2. Airflow - Orquestrador
   3. Spark - Processador de dados
   4. Jupyter - Para verificar arquivos python

Passo a passo para conhecer todos os processos:
1. Clone o repositório:

2. Instale o Docker Desktop:
   Instruções estão na documentação: https://docs.docker.com/desktop/setup/install/windows-install/

3. Ligue o Docker Desktop

4. Abra um terminal do powershell dentro da pasta onde está o docker-compose

5. Execute o comando:
   docker-compose up airflow-init
   docker-compose up airflow-webserver airflow-scheduler  minio spark spark-worker jupyter



## Monitoring/Alerting
Li alguns artigos, para conhecer mais das ferramentas de observabilidade, uma que gostei foi o grafana. O Grafana me possbilitaria  criar o que chamam de  "traces", onde eu poderia enviar ao grafana possibilidade de que ele me gere métricas que podem me indicar um gargalo, um processamento muito alto.
Grafana Também permite que alem das métricas, me gere logs do que foi executado, possibilitando que eu crie alertas e possa disparar esses alertas para times, pessoas em específico, a fim de dar possibilidade do time entrar com uma correção.
