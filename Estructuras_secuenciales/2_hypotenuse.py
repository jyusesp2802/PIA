#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

#Autor:Jaime Yust
#Fecha: 16/10/2025

print('Programa que calcula la hipotenusa de un triángulo rectángulo dado sus catetos')

leg1 = float(input("¿Cuánto mide el primer cateto? "))
leg2 = float(input('¿Cuanto mide el segundo cateto?'))

from math import sqrt

hypotenuse = sqrt((leg1**2)+(leg2**2))

print(f'La raiz cuadrada es {hypotenuse:.2f}')