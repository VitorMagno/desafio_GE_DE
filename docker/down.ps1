docker compose -f airflow\docker-compose-airflow.yaml down -v --remove-orphans
docker compose -f minio_e_metastore\compose.yml down -v --remove-orphans