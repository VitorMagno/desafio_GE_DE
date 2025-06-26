# desafio_GE_DE

Fiz o setup do MinIO, seguindo as instruções no docker hub. Lá descreve as instruções para um docker file, basta entender e converter para o formato do compose.

Para configurar o hive, li instruções no docker hub e a documentação do próprio hive. Um pouco mais complicado pois tive que baixar o ```postgresql-42.7.3.jar``` e buildar junto com a imagem que estava usando do hive. Toda configuração e environment foi baseada no docker hub e documentação

## subindo os serviços

Windows
```bash
docker network create datalakehouse
cd docker\powershell_scripts
init.ps1
```

use down.ps1 para desativar os serviços

Linux
```bash
docker network create datalakehouse
docker-compose \
  --env-file ./.env \
  -f docker/spark_jupyter/docker-compose.yml \
  -f docker/minio_e_metastore/compose.yml \
  up -d --build 
```
