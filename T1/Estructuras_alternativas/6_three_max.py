#Realiza un programa que pida tres números enteros y diga cuál es el mayor. No se puede usar la función max().

#Autor:Jaime Yust
#Fecha: 16/10/2025

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
num3 = int(input("Introduce el tercer número entero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El mayor número es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El mayor número es: {num2}")
else:
    print(f"El mayor número es: {num3}")