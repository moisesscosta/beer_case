# Apresentação
Demonstrar a arquitetura do tipo "medallion", com camadas de dados brutos(bronze layer), camada de dados processados(silver layer) e a camada de dados agregados(gold layer).

### Arquitetura
   Usei um docker para compor os componentes de que preciso
   Contem:
   
      1. Minio - Storage
      
      2. Airflow - Orquestrador
      
      3. Spark - Processador de dados
      
      4. Jupyter - Para verificar arquivos python

### Pré Requisitos:
   1. Instalar o python da url a seguir.
   Url: https://www.python.org/downloads/release/python-3913/
   2. Instalar JDK Java:
   Url: https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html

3. Instalar o jupyter notebook, eu utilizei a interface do anaconda navigator.
   Obs: Apenas para a execução local no computador
   Link> https://www.anaconda.com/download

### Passo a passo para conhecer todos os processos:
#### 1. Clone o repositório:
   Comando: https://github.com/moisesscosta/beer_case.git

#### 2. Instale o Docker Desktop:

   Instruções estão na documentação: https://docs.docker.com/desktop/setup/install/windows-install/

#### 3. Ligue o Docker Desktop

![image](https://github.com/user-attachments/assets/aec92f85-9c63-4375-a1bf-81ae07d6f727)

#### 4. Execute os arquivos de start_container_1 e start_container2, um em seguida do outro para iniciar os container
   Local: beer_case\docker

![image](https://github.com/user-attachments/assets/585ffb1e-bf2f-45ab-bc9b-fd5366a70d9c)

#### 5. Acesse o airflow:

   Logue no airflow com as credencias:
   login: airflow
   senha: airflow
   
![image](https://github.com/user-attachments/assets/38376707-0065-431a-8531-42d96ad680de)

#### 6. Clique na Dag:

![image](https://github.com/user-attachments/assets/90811971-40c8-4900-9959-1a7b4277be4d)

#### 7.Clique em Run dag:

![image](https://github.com/user-attachments/assets/038cdd6b-5250-463c-b23e-6d76fcfeccf0)

#### 8 Acesse o bucket com o minIO clicando na porta indicada, no caso localhost:9051:000
login: admin
senha: minioadmin

![image](https://github.com/user-attachments/assets/9ab66785-df64-446b-bddb-c19d9b817bb4)


#### 9.Veja o repositório com cada uma das camadas:

![image](https://github.com/user-attachments/assets/b406e951-c23d-4444-8c31-28be7ce8e0be)

#### 10. Entre no bronze-layer para ver os arquivos carregados:

![image](https://github.com/user-attachments/assets/a62aa3a4-ed18-45a4-b219-7d817286f758)

### Observações do processo.
   1. Eu não consegui finalizar a configuração da docker para rodar os processo de processamento de dados e agreagação dos dados na camada gold via DAG. Os arquivos da Dag onde está o script que seria carregado está no caminho:

      Caminho: beer_case\docker\airflow\dags\scripts


   2. Então eu montei localmente mesmo uma chamada do Spark para demonstrar como o dado parquet chegaria ao repositório do MinIO.
   3. Por eu fazer localmente o MinIO não se comunicou bem com o container
   4. O Container possui o Jupyter notebook porém como o Spark ficou configurado de forma incompleta não foi possível demonstrar a interação via docker.
   5. Na pasta \beer_case\docker\jupyter\work terá os arquivos de carga e de processamento da camada.

## Sobre monitoramento de alertas
Li alguns artigos, para conhecer mais das ferramentas de observabilidade, uma que gostei foi o grafana. O Grafana me possbilitaria  criar o que chamam de  "traces", onde eu poderia enviar ao grafana possibilidade de que ele me gere métricas que podem me indicar um gargalo, um processamento muito alto.
Grafana Também permite que alem das métricas, me gere logs do que foi executado, possibilitando que eu crie alertas e possa disparar esses alertas para times, pessoas em específico, a fim de dar possibilidade do time entrar com uma correção.

A primeira possibilidade seria agendar as rotinas via um parâmetro da Dag do Airflow, para garantir um schedule dos processos. A partir do Airflow também é possível identificar os logs de erros das dags e dos processos, já que o Airflow tem uma aba que contém todos os logs do que foi processado, interações, possibilidades de avisar times, via e-mail, via webhook.
