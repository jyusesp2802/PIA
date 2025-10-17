#Escribir un programa que lea un año indicar si es bisiesto (un año es bisiesto si es un número divisible por 4,
#pero no si es divisible por 100, excepto que también sea divisible por 400)

#Autor:Jaime Yust
#Fecha: 16/10/2025

year = int(input("Introduce un año para determinar si es bisiesto: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")

