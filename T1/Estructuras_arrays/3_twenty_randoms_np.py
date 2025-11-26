"""
Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy.
El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante)
y todos los números impares a las celdas restantes.
Utiliza arrays auxiliares si es necesario.

Autor: Jaime Yust
Fecha:26/11/2025
"""

import numpy as np

numbers = np.random.randint(0, 101, size=20)
print("Array original:")
print(numbers)

even_numbers = numbers[numbers % 2 == 0]
odd_numbers = numbers[numbers % 2 != 0]

to_combine = np.concatenate((even_numbers, odd_numbers))

print("Array con pares primero y luego impares:")
print(to_combine)