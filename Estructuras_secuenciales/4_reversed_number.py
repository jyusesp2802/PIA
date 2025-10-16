#Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

#Autor:Jaime Yust
#Fecha: 16/10/2025

number = int(input('¿Dame un número de dos cifras?'))

unit_1 = abs(number)//10  #Calcula la primera unidad
unit_2 = abs(number)%10   #Calcula la segunda unidad

reversed_number = unit_2*10 + unit_1

print(reversed_number)