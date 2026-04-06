from scripts import cargar as ld
from scripts import extraer as ext
from scripts import transformar as trf


# 1. Extracción y Limpieza
# Ruta especifica de los archivos dentro del directorio
archivo_stock = "./data/raw/registro_stock.xlsx"
archivo_movimientos = "./data/raw/registro_movimientos.xlsx"

# Extracción de los datos para ser transformados a un objeto tipo Data Frame
df_stock = ext.extraer_dataframe(archivo_stock)
df_movimientos = ext.extraer_dataframe(archivo_movimientos)

# Formateo y limpieza de cada columna de los Data Frame extraidos
df_stock_formateado = trf.limpiar_columnas(df_stock)
df_movimientos_formateado = trf.limpiar_columnas(df_movimientos)


# 2. Definición de las tablas necesarias
# Transformar los Data Frame de ventas y devoluciones en tablas de hechos
df_dtventas = trf.convertir_dataventas(df_movimientos_formateado)
df_dtdevoluciones = trf.convertir_datadevoluciones(df_movimientos_formateado)


# Creación de las dimensiones 'Producto' y 'Categoría'
dimension_productos=trf.dimension_productos(df_stock_formateado)
dimension_productos = trf.integrar_ranking(df_dtventas,df_dtdevoluciones,dimension_productos)
dimension_categorias=trf.dimension_categorias(df_stock_formateado)


# 3. Exportación de datos al archivo final (el nombre del documento se encuentra dentro de la función 'Exportar Datos')
lista_hojas = [dimension_categorias,df_dtventas,df_dtdevoluciones]
lista_nombres = ["dimcategoria","dtventas","dtdevoluciones"]
ld.exportar_datos(dimension_productos,lista_hojas,lista_nombres)