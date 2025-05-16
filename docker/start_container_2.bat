mkdir .\postgres\postgres-db-volume\pg_stat
mkdir .\postgres\postgres-db-volume\pg_tblspc

echo "inicinado containers"
echo
docker-compose up airflow-webserver airflow-scheduler minio spark-master spark-worker jupyter
 
pause
