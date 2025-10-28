"""
Escribe un programa que genere 20 números enteros entre 100 y 999.
Estos números se deben introducir en una lista de 4 filas por 5 columnas.
El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo.
La suma total debe aparecer en la esquina inferior derecha.

Autor: Jaime Yust
Fecha: 24/10/2025

"""

import random

rows = 4
cols = 5

# Crear la matriz y llenarla con números aleatorios
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(100, 999))
    matrix.append(row)
# Calcular sumas parciales de filas
row_sums = [sum(row) for row in matrix]
# Calcular sumas parciales de columnas
col_sums = [sum(matrix[i][j] for i in range(rows)) for j
            in range(cols)]
# Calcular suma total
total_sum = sum(row_sums)
# Mostrar la matriz con sumas parciales
print(f"{'':<6}", end="")
for j in range(cols):
    print(f"Col{j + 1:<6}", end="")
print("RowSum")
for i in range(rows):
    print(f"Row{i + 1:<5}", end="")
    for j in range(cols):
        print(f"{matrix[i][j]:<6}", end="")
    print(f"{row_sums[i]}")
# Mostrar sumas parciales de columnas
print("ColSum", end="")
for j in range(cols):
    print(f"{col_sums[j]:<6}", end="")
print(f"{total_sum}")




