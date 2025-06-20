import openmeteo_requests
import pandas as pd
import requests
import requests_cache
import time
from retry_requests import retry

# Lista de capitais brasileiras (padrão para validação)
CAPITAIS_BRASIL = {
    "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília",
    "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte",
    "Belém", "João Pessoa", "Recife", "Teresina", "Rio de Janeiro", "Natal",
    "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo",
    "Aracaju", "Palmas"
}

def get_coordinates(locais):
    lista_coordenadas = []
    session = requests_cache.CachedSession('.geocoding_cache', expire_after=86400)  # 1 dia de cache

    for local in locais:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={local}&count=10&language=en&format=json"
        success = False

        for tentativa in range(5):  # Retry até 5 vezes
            try:
                response = session.get(url, timeout=5)
                response.raise_for_status()
                data = response.json()

                # Validar se o resultado corresponde a uma capital brasileira
                for result in data.get("results", []):
                    feature_code = result.get("feature_code", "")
                    country_code = result.get("country_code", "")

                    if feature_code == "PPLC" and country_code == "BR":
                        latitude = result["latitude"]
                        longitude = result["longitude"]
                        lista_coordenadas.append((latitude, longitude))
                        success = True
                        break  # Achou a capital, pode sair do loop dos resultados
                
            except Exception as e:
                print(f"Erro ao consultar '{local}': {e}. Tentando novamente ({tentativa + 1}/5)...")
                time.sleep(2)  # Espera 2 segundos antes de tentar novamente

        if not success:
            raise RuntimeError(f"Falha ao obter coordenadas para '{local}' após múltiplas tentativas.")

    return lista_coordenadas

def consulta_api(coordenadas):
    # Setup Open-Meteo API com retry e cache
    cache_session = requests_cache.CachedSession('.weather_cache', expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://archive-api.open-meteo.com/v1/archive"
    current_date = pd.Timestamp.now(tz="UTC").strftime("%Y-%m-%d")
    params = {
        "latitude": coordenadas[0],
        "longitude": coordenadas[1],
        "start_date": "2015-01-03",
        "end_date": current_date - pd.Timedelta(days=2),
        "hourly": "temperature_2m",
        "timezone": "auto"
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )}

    hourly_data["temperature_2m"] = hourly_temperature_2m

    hourly_dataframe = pd.DataFrame(data=hourly_data)
    return hourly_dataframe

def get_data_historical():
    capitais = list(CAPITAIS_BRASIL)
    coordenadas_list = get_coordinates(capitais)

    for coordenadas in coordenadas_list:
        df = consulta_api(coordenadas)
    
    return df

if __name__ == "__main__":
    get_data_historical()
