docker compose -f ..\airflow\compose.yaml up -d
docker compose -f ..\minio_e_metastore\compose.yml up -d
..\minio_e_metastore\windows_bash\first_setup.ps1
docker compose -f ..\spark_jupyter\compose.yml up -d