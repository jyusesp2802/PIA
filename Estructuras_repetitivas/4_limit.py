"""
En un programa que pida el limite inferior y superior de un intervalo.
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.

Autor:Jaime Yust
Fecha: 16/10/2025

"""
print('Este programa pide un intervalo y luego números para analizar su posición respecto al intervalo.')

sum_range = 0
out_range_count = 0
equal_limit = False

lower_range = int(input("Introduce el límite inferior del intervalo: "))
upper_range = int(input("Introduce el límite superior del intervalo: "))


while lower_range >= upper_range:
    print("Error: El límite inferior debe ser menor que el límite superior.")
    lower_range = int(input("Introduce el límite inferior del intervalo: "))
    upper_range = int(input("Introduce el límite superior del intervalo: "))

num = int(input("Introduce un número (0, para salir): "))

while num != 0:
    if lower_range < num < upper_range:  # Pertenece al intervalo
        sum_range += num
    else:  # No pertenece al intervalo
        out_range_count += 1
        # Número igual a alguno de los límites
        if num == lower_range or num == upper_range:
            equal_limit = True
    num = int(input("Introduce un número (0, para salir): "))


print(f"La suma de los números dentro del intervalo es {sum_range}")
print(f"La cantidad de números fuera del intervalo es {out_range_count}")
if equal_limit:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")









