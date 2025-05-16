# Apresentação
Demonstrar a arquitetura do tipo "medallion", com camadas de dados brutos(bronze layer), camada de dados processados(silver layer) e a camada de dados agregados(gold layer).

### Arquitetura
Usei um docker para compor os componentes de que preciso
Contem:
   1. Minio - Storage
   2. Airflow - Orquestrador
   3. Spark - Processador de dados
   4. Jupyter - Para verificar arquivos python

### Passo a passo para conhecer todos os processos:
#### 1. Clone o repositório:

#### 2. Instale o Docker Desktop:
   Instruções estão na documentação: https://docs.docker.com/desktop/setup/install/windows-install/

#### 3. Ligue o Docker Desktop

![image](https://github.com/user-attachments/assets/aec92f85-9c63-4375-a1bf-81ae07d6f727)

#### 4. Execute os arquivos de start_container_1 e start_container2, um em seguida do outro para iniciar os container
Local: beer_case\docker

![image](https://github.com/user-attachments/assets/585ffb1e-bf2f-45ab-bc9b-fd5366a70d9c)

Acesse o airflow:

Logue no airflow com as credencias:
login: airflow
senha: airflow:
![image](https://github.com/user-attachments/assets/38376707-0065-431a-8531-42d96ad680de)

Clique na Dag:

![image](https://github.com/user-attachments/assets/90811971-40c8-4900-9959-1a7b4277be4d)

Clique em Run dag:

![image](https://github.com/user-attachments/assets/038cdd6b-5250-463c-b23e-6d76fcfeccf0)

Acesse o bucket com o minIO clicando na porta indicada, no caso localhost:9051:000
login: admin
senha: minioadmin

![image](https://github.com/user-attachments/assets/9ab66785-df64-446b-bddb-c19d9b817bb4)


Veja o repositório com cada uma das camadas:

![image](https://github.com/user-attachments/assets/b406e951-c23d-4444-8c31-28be7ce8e0be)

Entre no bronze-layer para ver os arquivos carregados:

![image](https://github.com/user-attachments/assets/a62aa3a4-ed18-45a4-b219-7d817286f758)


## Monitoring/Alerting
Li alguns artigos, para conhecer mais das ferramentas de observabilidade, uma que gostei foi o grafana. O Grafana me possbilitaria  criar o que chamam de  "traces", onde eu poderia enviar ao grafana possibilidade de que ele me gere métricas que podem me indicar um gargalo, um processamento muito alto.
Grafana Também permite que alem das métricas, me gere logs do que foi executado, possibilitando que eu crie alertas e possa disparar esses alertas para times, pessoas em específico, a fim de dar possibilidade do time entrar com uma correção.
