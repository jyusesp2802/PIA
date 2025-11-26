"""
Haz lo mismo que en el ejercicio anterior pero usando la libreria numpy

Autor: Jaime Yust
Fecha:26/11/2025

"""

import numpy as np

numbers = np.random.randint(0, 101, size=20)

squares = numbers ** 2
cubes = numbers ** 3

print(f"{'Number':<10}{'Square':<10}{'Cube':<10}")

for num, sq, cb in zip(numbers, squares, cubes):
    print(f"{num:<10}{sq:<10}{cb:<10}")