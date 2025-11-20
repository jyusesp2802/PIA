"""
Escribe un programa que genere 20 números enteros entre 100 y 999.
Estos números se deben introducir en una lista de 4 filas por 5 columnas.
El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo.
La suma total debe aparecer en la esquina inferior derecha.

Autor: Jaime Yust
Fecha: 24/10/2025

"""
from random import randint

rows = 3
columns = 2
low_num = 100
big_num = 999
width_num = 5

array = [[randint(low_num, big_num) for _ in range(columns)] for _ in range(rows)]

# Mostrar filas y sumatorio de cada fila
for row in array:
    sum_row = 0
    for n in row:
        sum_row += n
        print(f"{n:{width_num}} ", end="")
    print(f"| {sum_row:{width_num}}")

# Mostrar sumatorio de las columnas y del total
len_sep = ((width_num + 1) * (columns + 1) + 1)
print("-" * len_sep)  # separador
sum_total = 0
for column in range(columns):
    sum_column = 0
    for row in range(rows):
        sum_column += array[row][column]
    print(f"{sum_column:{width_num}} ", end="")
    sum_total += sum_column
print(f"| {sum_total:{width_num}}")




