docker compose -f airflow\docker-compose-airflow.yaml up -d
docker compose -f minio_e_metastore\compose.yml up -d
.\minio_e_metastore\first_setup.ps1