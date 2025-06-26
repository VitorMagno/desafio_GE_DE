docker compose -f ..\airflow\compose.yaml down
docker compose -f ..\minio_e_metastore\compose.yml down
docker compose -f ..\spark_jupyter\compose.yml down