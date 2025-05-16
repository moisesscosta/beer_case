echo "limpando containers e iniciando ambiente"
FOR /f "tokens=*" %%i IN ('docker ps -q -a') DO docker stop %%i
FOR /f "tokens=*" %%i IN ('docker ps -q -a') DO docker rm %%i
echo "inicinado containers"
echo
docker-compose up -d airflow-init
 
pause
