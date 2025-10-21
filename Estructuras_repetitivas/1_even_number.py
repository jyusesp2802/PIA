#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

#Autor:Jaime Yust
#Fecha: 16/10/2025

print('Este programa imprime todos los números pares entre dos números enteros que introduzcas.')

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

print(f"Números pares entre {num1} y {num2}:")

for number in range(num1, num2 + 1):
    if number % 2 == 0:
        print(number)

