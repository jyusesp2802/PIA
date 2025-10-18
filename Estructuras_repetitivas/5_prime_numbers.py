#Crea un programa que pida un número por teclado al usuario y diga si es primo. En caso de que no se introduzca un número o que esta sea menor que 2 se debe mostrar un mensaje de error.

#Autor:Jaime Yust
#Fecha: 16/10/2025

prime_number = int(input("Por favor, introduzca un número: "))


while True:
    if prime_number <2:
        print("Error: El número debe ser mayor o igual a 2.")
        prime_number = int(input("Por favor, introduzca un número: "))
    else:
        if prime_number >=2:
            for i in range(2, int(prime_number**0.5) + 1):
                if prime_number % i == 0:
                    print(f"El número {prime_number} no es primo.")
                    break
            else:
                print(f"El número {prime_number} es primo.")
        break

