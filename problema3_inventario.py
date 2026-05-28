# Fase 5 - Evaluación Final POA
# Curso: Fundamentos de Programación
# Estudiante: Carol Yulieth Díaz Calderón
# Problema 3: Auditoría de inventario y reabastecimiento

def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """
    Calcula la cantidad exacta que se debe pedir de un artículo.
    Si el stock actual es menor al stock mínimo, se pide la diferencia.
    Si el stock actual es suficiente, se pide cero.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# Matriz de inventario:
# [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
inventario = [
    ["A001", "Mouse", 8, 15],
    ["A002", "Teclado", 20, 10],
    ["A003", "Monitor", 4, 8],
    ["A004", "Cable HDMI", 30, 25],
    ["A005", "Memoria USB", 5, 12],
    ["A006", "Disco Duro", 7, 7]
]


print("AUDITORÍA DE INVENTARIO Y REABASTECIMIENTO")
print("-" * 65)
print("Artículo                 Stock actual   Stock mínimo   Cantidad a pedir")
print("-" * 65)

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_cantidad_pedir(stock_actual, stock_minimo)

    print(f"{codigo} - {nombre:<15} {stock_actual:<14} {stock_minimo:<13} {cantidad_pedir}")

print("-" * 65)
print("Proceso finalizado.")
