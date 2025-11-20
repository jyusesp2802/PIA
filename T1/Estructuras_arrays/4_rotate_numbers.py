"""
Escribe un programa que lea 5 números por teclado y que los almacene en una lista. Rota los elementos de esa lista, es decir,
el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc.
El número que se encuentra en la última posición debe pasar a la posición 0. Finalmente, muestra el contenido de la lista.

Autor: Jaime Yust
Fecha: 24/10/2025

"""

numbers = []
for i in range(5):
    try:
        num = int(input(f'Introduce el número {i + 1}: '))
    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")
        num = int(input(f'Introduce el número {i + 1}: '))

    numbers.append(num)

rotated_numbers = [numbers[-1]] + numbers[:-1]
print('Lista rotada:', rotated_numbers)
