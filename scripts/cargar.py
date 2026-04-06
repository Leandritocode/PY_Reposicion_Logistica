import pandas as pd

# Crea el documento en excel y agrega las hojas fundamentales para el análisis
def exportar_datos(df_base,lista_hojas,lista_nombres):
    ruta = f"./data/clean/registro_preparado.xlsx"
    df_base.to_excel(ruta,sheet_name="dimproducto",index=False)
    with pd.ExcelWriter(ruta,mode="a",engine="openpyxl") as write:
        for hoja,nombre in zip(lista_hojas,lista_nombres):
            hoja.to_excel(write,sheet_name=nombre,index=False)