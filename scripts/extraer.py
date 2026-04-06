import pandas as pd


# Extrae la información de los documentos excel origen y los transforma en Data Frame
def extraer_dataframe(origen):
    df_origen = pd.read_excel(origen)
    return df_origen