#Escribe un programa que pida el limite inferior y superior de un intervalo.
#Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
#A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

#La suma de los números que están dentro del intervalo (intervalo abierto).
#Cuantos números están fuera del intervalo.
#Informa si hemos introducido algún número igual a los límites del intervalo.

#Autor:Jaime Yust
#Fecha: 16/10/2025

lower_limit = int(input("Por favor, introduzca el límite inferior del intervalo: "))
upper_limit = int(input("Por favor, introduzca el límite superior del intervalo: "))


while lower_limit >= upper_limit:
    print("Error: El límite inferior debe ser menor que el límite superior.")
    lower_limit = int(input("Por favor, introduzca el límite inferior del intervalo: "))
    upper_limit = int(input("Por favor, introduzca el límite superior del intervalo: "))

sum__interval = 0
count_outside_interval = 0
equal_to_limits = False

while True:
    number = int(input("Introduce un número (0 para terminar): "))
    if number == 0:
        break
