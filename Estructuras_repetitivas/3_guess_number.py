"""
Crea una aplicación que permita adivinar un número.
La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
además de los intentos que te quedan (tienes 10 intentos para acertarlo).
El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado),
si se llega al limite de intentos te muestra el número que había generado.

Autor:Jaime Yust
Fecha: 16/10/2025
"""

print('Este programa te permite adivinar un número entre 1 y 100.')

import random
number_to_guess = random.randint(1, 100)

attempts = 10
attempts_used = 0

print("¡Bienvenido al juego de adivinar el número!")

while attempts > 0:
    user_guess = int(input("Introduce un número entre 1 y 100: "))
    attempts_used += 1

    if user_guess < number_to_guess:
        attempts -= 1
        print(f"El número a adivinar es mayor. Te quedan {attempts} intentos.")
    elif user_guess > number_to_guess:
        attempts -= 1
        print(f"El número a adivinar es menor. Te quedan {attempts} intentos.")
    else:
        print(f"¡Felicidades! Has adivinado el número {number_to_guess} en {attempts_used} intentos.")
        break
else:
    print(f"Lo siento, has agotado tus intentos. El número era {number_to_guess}.")


