#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
#El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

#Autor:Jaime Yust
#Fecha: 16/10/2025

numbers_count = int(input("¿Cuántos números deseas introducir?: "))

zero = 0
positive = 0
negative = 0

for count in range(numbers_count):
    number = float(input(f"Introduce el número {count + 1}: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1
print(f"Números mayores que 0: {positive}")
print(f"Números menores que 0: {negative}")
print(f"Números iguales a 0: {zero}")
