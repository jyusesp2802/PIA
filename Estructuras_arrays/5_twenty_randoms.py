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

numbers = [[0] * cols for _ in range(rows)]

for row in range(rows):
    for columns in range(cols):
        numbers[row][columns] = random.randint(100, 999)

for rows in range(rows):
    row_sum = 0
    for columns in range(cols):
        print(f"{numbers[rows][columns]:>6}", end="")
        row_sum += numbers[rows][columns]
    print(f" |{row_sum:>6}")






