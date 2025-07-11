import requests
import pandas as pd

# URL del API
url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=1000"

# Hacemos la petición
response = requests.get(url)

# Convertimos la respuesta JSON a un diccionario
data = response.json()

records = data[1]

df = pd.json_normalize(records)
df = df[["country.id", "country.value", "value", "date"]]
df.columns = ["pais_id", "nombre_pais", "poblacion", "año"]
df.dropna(inplace=True)

df.to_json("poblacion.json", orient="records")
