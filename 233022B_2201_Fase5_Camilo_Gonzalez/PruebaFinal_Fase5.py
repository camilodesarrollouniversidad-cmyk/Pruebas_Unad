# Programa para auditar inventario y calcular
# la cantidad de articulos que necesitan ser reabastecidos.


# funcion para calcular la cantidad a pedir
def cantidad_a_pedir(stock_actual, stock_minimo):
  
    # si el stock actual es menor al mínimo, se debe pedir la diferencia entre ambos, de lo contrario no se debe pedir nada (0 unidades)
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

# lista de artículos con su código, nombre, stock actual y stock mínimo

articulos = [
    [101, "esfero", 12, 20],
    [102, "Cuaderno", 25, 15],
    [103, "Resaltador", 5, 10],
    [104, "Carpeta", 6, 8],
    [105, "Regla", 3, 12],
    [106, "borrador", 20, 25],
    [107, "sacapuntas", 8, 10],
    [108, "Pegante", 15, 20],
    [109, "Tijeras", 4, 6],
    [110, "Cinta adhesiva", 10, 15],
    [111, "Marcador", 12, 12],

]

# programa principal
if __name__ == "__main__":
    print("Lista de pedidos:")
   # se recorre la lista de artículos y se calcula la cantidad a pedir para cada uno, mostrando solo aquellos que necesitan ser pedidos 
    for codigo, nombre, stock_actual, stock_minimo in articulos:
        pedir = cantidad_a_pedir(stock_actual, stock_minimo)
        if pedir > 0:
            print(f"- {nombre}: {pedir} unidad(es)")
