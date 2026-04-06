import pandas as pd
import datetime as dt
from scripts import operaciones as opc


# Formatea las columanas y sus valores, emité alertas de procesos y define los tipos de datos correspondientes y gestionando valores nulos bajo criterios de impacto en el análisis
def limpiar_columnas(df_origen):
    df_resultado = df_origen.copy()
    df_resultado.columns = df_resultado.columns.str.strip().str.lower()
    columnas_necesarias = ["codigo","fecha"]
    lista_enteros = ["cantidad"]
    for columna in df_resultado.columns:
        if columna != "fecha":
            try:
                df_resultado[columna] = df_resultado[columna].astype(float).round(2)
                valores_nulos = df_resultado[columna].isna().sum()
                if valores_nulos > 0:
                    print(f"🚨 Se detectaron {valores_nulos} celdas vacias en la columna {columna}")
                    df_resultado[columna] = df_resultado[columna].fillna(0)
                    print(f"Se reemplazaron {valores_nulos} celdas vacias de la columna {columna} con '0'")
            except ValueError:
                valores_nulos = df_resultado[columna].isna().sum()
                if valores_nulos > 0:
                    print(f"🚨 Se detectaron {valores_nulos} celdas vacias en la columna {columna}")
                    if columna in columnas_necesarias:
                        df_resultado = df_resultado.dropna(subset=[columna])
                        print(f"🆑 Se eliminaron {valores_nulos} celdas vacias de la columna {columna}")
                    else:
                        df_resultado[columna] = df_resultado[columna].fillna("-")
                        print(f"📄 Se reemplazaron {valores_nulos} celdas vacias de la columna {columna} con '-'")
            if columna in lista_enteros:
                df_resultado[columna] = df_resultado[columna].astype(int)
            else:
                df_resultado[columna] = df_resultado[columna].astype(str).str.upper()
        else:
            df_resultado[columna] = pd.to_datetime(df_resultado[columna]).dt.date
    return df_resultado


# Realiza un filtro del Data Frame de ventas con todas las operaciones destinadas a SOCIOS/CLIENTES (Venta) y resumiendo la matriz con información crucial y necesaria en el proceso de administrar las relaciones entre tablas
def convertir_dataventas(df_transformado):
    df_resultado = df_transformado.copy()
    df_resultado = df_resultado[df_resultado["hasta"] == "SOCIOS/CLIENTES"]
    df_resultado = df_resultado.rename(columns={"cantidad":"cantidad_venta"})
    df_resultado = df_resultado[["fecha","codigo","categoria","cantidad_venta"]]
    return df_resultado


# Realiza un filtro del Data Frame de devoluciones con todas las operaciones provenientes de SOCIOS/CLIENTES (Venta) y resumiendo la matriz con información crucial y necesaria en el proceso de administrar las relaciones entre tablas
def convertir_datadevoluciones(df_transformado):
    df_resultado = df_transformado.copy()
    df_resultado = df_resultado[df_resultado["desde"] == "SOCIOS/CLIENTES"]
    df_resultado = df_resultado.rename(columns={"cantidad":"cantidad_devolucion"})
    df_resultado = df_resultado[["fecha","codigo","categoria","cantidad_devolucion"]]
    return df_resultado


# Crea la primera dimensión 'Productos',  integrando información critica vinculada al control y estado actual de los productos del almacén
def dimension_productos(df_stock):
    df_resultado = df_stock.copy()
    df_resultado = df_resultado.drop_duplicates(subset=["codigo","nombre"],keep ="last")
    df_resultado = df_resultado[["codigo","nombre","categoria","cantidad","coste"]]
    return df_resultado

# Calcula e integra el ranking por ventas netas de cada codigo a la dimensión 'Productos'
def integrar_ranking(df_ventas,df_devoluciones,dimension_stock):
    df_ventas_resultado = df_ventas.groupby("codigo")["cantidad_venta"].sum().reset_index()
    df_devoluciones_resultado = df_devoluciones.groupby("codigo")["cantidad_devolucion"].sum().reset_index()
    df_resultado = pd.merge(df_ventas_resultado,df_devoluciones_resultado,on="codigo",how="left")
    df_resultado["cantidad_devolucion"] = df_resultado["cantidad_devolucion"].fillna(0)
    df_resultado["venta_neto"] = df_resultado.apply(opc.transformar_negativo,axis=1)
    df_resultado["ranking"] = df_resultado["venta_neto"].rank(method="first",ascending=False)
    df_resultado = df_resultado.sort_values(by="ranking")
    df_resultado = pd.merge(dimension_stock,df_resultado,on="codigo",how="left")
    df_resultado = df_resultado[["codigo","nombre","categoria","cantidad","coste","ranking"]]
    df_resultado["ranking"] = df_resultado["ranking"].fillna(0)
    return df_resultado

# Crea la segunda dimensión 'Categorias', la cual contiene información unica de las categorias existentes
def dimension_categorias(df_stock):
    df_resultado = df_stock.copy()
    df_resultado = df_resultado.drop_duplicates(subset=["categoria"],keep="last")
    df_resultado = df_resultado[["categoria"]]
    return df_resultado