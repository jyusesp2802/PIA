#Crea un programa que muestre en pantalla los N primeros número primos. El valor de N se pide por teclado al usuario/a.

#Autor:Jaime Yust
#Fecha: 16/10/2025

print('Este programa muestra los N primeros números primos.')

n = int(input("Por favor, introduzca el valor de la cantidad de números primos que deseas: "))

count = 0  # Contador de números primos encontrados
num = 2    # Número actual a comprobar
primes = [] # Lista para almacenar los números primos encontrados

while count < n:
    for prime in range(2, int(num**0.5) + 1):
        if num % prime == 0:
            break
    else:
        primes.append(num)
        count += 1
    num += 1

print(f"Los primeros {n} números primos son: {primes}")
