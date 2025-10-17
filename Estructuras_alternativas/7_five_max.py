#Realiza un programa que pida cinco números enteros y diga cuál es el mayor No se puede usar la función max()..

#Autor:Jaime Yust
#Fecha: 16/10/2025

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
num3 = int(input("Introduce el tercer número entero: "))
num4 = int(input("Introduce el cuarto número entero: "))
num5 = int(input("Introduce el quinto número entero: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    print(f"El mayor número es: {num1}")
elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
    print(f"El mayor número es: {num2}")
elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    print(f"El mayor número es: {num3}")
elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    print(f"El mayor número es: {num4}")
else:
    print(f"El mayor número es: {num5}")
