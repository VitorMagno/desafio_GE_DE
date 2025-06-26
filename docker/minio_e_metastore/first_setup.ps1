# Variáveis
$alias = "datalake"
$endpoint = "http://localhost:9000"
$accessKey = "minio"
$secretKey = "minio123"
$bucket = "warehouse"

# Configura o alias
Write-Host "Configurando alias '$alias'..."
mc alias set $alias $endpoint $accessKey $secretKey

# Verifica se o bucket já existe
try {
    mc ls "$alias/$bucket" | Out-Null
    Write-Host "Bucket '$bucket' já existe."
}
catch {
    Write-Host "Bucket '$bucket' não existe. Criando..."
    mc mb "$alias/$bucket"
}