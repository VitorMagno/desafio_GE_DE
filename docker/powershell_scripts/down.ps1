docker compose -f ..\airflow\compose.yaml down -v --remove-orphans
docker compose -f ..\minio_e_metastore\compose.yml down -v --remove-orphans
docker compose -f ..\spark_jupyter\compose.yml down -v --remove-orphans