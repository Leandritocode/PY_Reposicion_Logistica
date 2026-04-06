# Compara el resultado de la operación, un dato negativo representa un posible error de usuario al retornar los productos del albarán al stock sin aportar un valor al análisis
def transformar_negativo(fila):
    if fila["cantidad_venta"] - fila["cantidad_devolucion"] < 1:
        return 0
    else:
        return fila["cantidad_venta"] - fila["cantidad_devolucion"]