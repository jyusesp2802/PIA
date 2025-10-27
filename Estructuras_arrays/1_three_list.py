"""
Define tres listas de 20 números enteros cada uno, con nombres number, square y cube.
Carga las lista number con valores aleatorios entre 0 y 100.
En la lista square se deben almacenar los cuadrados de los valores que hay en number.
En la lista cube se deben almacenar los cubos de los valores que hay en number.
A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.

Autor: Jaime Yust
Fecha: 24/10/2025

"""
import random

number = []
square = []
cube = []

for _ in range(20):
    num = random.randint(0, 100)
    number.append(num)
    square.append(num ** 2)
    cube.append(num ** 3)
print(f"{'Number':<10}{'Square':<10}{'Cube':<10}")
for i in range(20):
    print(f"{number[i]:<10}{square[i]:<10}{cube[i]:<10}")






