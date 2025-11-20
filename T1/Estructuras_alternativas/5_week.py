#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
#Si introducimos otro número nos da un error.

#Autor:Jaime Yust
#Fecha: 16/10/2025

day_number = int(input("Introduce un número del 1 al 7 para saber el día de la semana: "))
if day_number == 1:
    print("Lunes")
elif day_number == 2:
    print("Martes")
elif day_number == 3:
    print("Miércoles")
elif day_number == 4:
    print("Jueves")
elif day_number == 5:
    print("Viernes")
elif day_number == 6:
    print("Sábado")
elif day_number == 7:
    print("Domingo")
else:
    print("Error: Número inválido. Por favor, introduce un número del 1 al 7.")