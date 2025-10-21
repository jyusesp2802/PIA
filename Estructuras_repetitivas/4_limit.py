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

lower_range = int(input("Introduce el límite inferior del intervalo: "))
upper_range = int(input("Introduce el límite superior del intervalo: "))

sum_range = 0
out_range_count = 0
equal_limit = False

while lower_range >= upper_range:
    print("Error: El límite inferior debe ser menor que el límite superior.")
    lower_range = int(input("Introduce el límite inferior del intervalo: "))
    upper_range = int(input("Introduce el límite superior del intervalo: "))
else:










