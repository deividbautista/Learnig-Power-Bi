import requests
import pandas as pd
from models.SaveDataDoc import savDocData

countries = [
    "ARG",
    "BRA",
    "MEX",
    "COL",
    "CHL",
    "PER",
    "ESP",
    "USA",
    "CAN",
    "GBR",
    "JPN",
    "AUS",
    "UK",
    "DEU",
    "CHN",
]
indicators = {
    "NY.GDP.MKTP.CD": "PIB_total_USD",
    "NY.GDP.PCAP.CD": "PIB_per_capita_USD",
    "FP.CPI.TOTL.ZG": "Inflacion_anual_porcentaje",
    "SL.UEM.TOTL.ZS": "Desempleo_porcentaje",
    "NE.EXP.GNFS.CD": "Exportaciones_USD",
    "DT.DOD.DECT.CD": "Deuda_externa_USD",
    "BX.KLT.DINV.CD.WD": "Inversion_extranjera_USD",
    "SE.XPD.TOTL.GD.ZS": "Gasto_educacion_porcentaje_PIB",
}
years = "1990:2020"


def getAllData(country, indicator, years):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&date={years}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error al obtener los datos del API")

    data = response.json()

    if len(data) > 1 and data[1]:  # Si hay datos en la segunda parte del JSON
        return pd.json_normalize(data[1])  # Retorna un DataFrame
    else:
        return pd.DataFrame()  # Retorna vacío si no hay datos


endData = pd.DataFrame()  # DataFrame vacío para acumular resultados

for country in countries:
    for id_indicator, name_indicator in indicators.items():
        df_temp = getAllData(country, id_indicator, years)
        if not df_temp.empty:
            df_temp["pais"] = country
            df_temp["indicador"] = name_indicator
            endData = pd.concat([endData, df_temp], ignore_index=True)

if not endData.empty:
    finalData = endData.pivot_table(
        index=["pais", "date"], columns="indicador", values="value", aggfunc="first"
    ).reset_index()

    # Llenamos los valores vacios con 0
    finalData = finalData.fillna(0)

    savDocData(finalData, "datafull.json")
    # Guardar como JSON (orientación "records" para lista de diccionarios)
    # finalData.to_json("data.json", orient="records")
else:
    print("No se encontraron datos para los filtros aplicados.")
