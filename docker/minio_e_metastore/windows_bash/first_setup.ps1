# Define o alias dentro do container
docker exec minio_e_metastore-datalake-1 mc alias set datalake http://localhost:9000 admin admin123

# Testa se o bucket existe dentro do container e captura o código de saída
$bucketCheck = docker exec minio_e_metastore-datalake-1 sh -c "mc ls datalake/warehouse > /dev/null 2>&1"

if ($LASTEXITCODE -eq 0) {
    Write-Host "Bucket já existe."
} else {
    Write-Host "Criando bucket..."
    docker exec minio_e_metastore-datalake-1 mc mb datalake/warehouse
}
