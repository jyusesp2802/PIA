"""
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones:
sumar, restar, multiplicar, dividir y terminar.
Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación.
Si se introduce una opción incorrecta se muestra un mensaje de error. El menú se volverá a mostrar, a menos que no se de a la opción terminar.
Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera).
Las variables se inicializan a cero.
Modifica el programa anterior para que si no se introducen las dos variables desde
la opción correspondiente no se puedan ejecutar el resto de las opciones.
Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas,
pide una opción (por su número) y devuelve la opción escogida. Modifica el último programa para que use esta función.

Autor: Jaime Yust
Fecha: 23/10/2025

"""

print('Calculadora básica')

def sumar (a, b):
    return a + b

def restar (a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: División por cero'

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Introducir nuevos valores")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Terminar")
    opcion = input("Elige una opción (1-6): ")
    return opcion



while True:
    opcion = mostrar_menu()
    if opcion == '1':
        while True:
            try:
                value_a = float(input('Introduce el valor de a: '))
                value_b = float(input('Introduce el valor de b: '))
                valores_introducidos = True  # Ahora podemos hacer operaciones
                break
            except ValueError:
                print('Error: Por favor, introduce valores numéricos válidos.')
    elif opcion in ['2', '3', '4', '5']:
        if not valores_introducidos:
            print("Error: primero debes introducir los valores (opción 1).")
            continue
        if opcion == '2':
            resultado = sumar(value_a, value_b)
            print(f'El resultado de sumar es: {resultado}')
        elif opcion == '3':
            resultado = restar(value_a, value_b)
            print(f'El resultado de restar es: {resultado}')
        elif opcion == '4':
            resultado = multiplicar(value_a, value_b)
            print(f'El resultado de multiplicar es: {resultado}')
        elif opcion == '5':
            resultado = dividir(value_a, value_b)
            print(f'El resultado de dividir es: {resultado}')
    elif opcion == '6':
        print("Terminando el programa.")
        break
    else:
        print("Opción incorrecta. Por favor, elige una opción válida.")