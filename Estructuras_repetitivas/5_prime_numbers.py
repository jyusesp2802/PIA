#Crea un programa que pida un número por teclado al usuario y diga si es primo. En caso de que no se introduzca un número o que esta sea menor que 2 se debe mostrar un mensaje de error.

#Autor:Jaime Yust
#Fecha: 16/10/2025

prime_number = int(input("Por favor, introduzca un número: "))


while prime_number :
    if prime_number < 2:
        print("Error: El número debe ser mayor o igual a 2.")
        break
    for i in range(2, int(prime_number ** 0.5) + 1): #comprueba si la raiz cuadrada des diviisible
        if prime_number % i == 0: #si es divisible no es primo
            print(f"El número {prime_number} no es primo.")
            break
    else:
        print(f"El número {prime_number} es primo.")
    break