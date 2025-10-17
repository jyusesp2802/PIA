#Escribir un programa que que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros.
#Hay billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.

#Autor:Jaime Yust
#Fecha: 16/10/2025

amount = int(input("Introduce una cantidad exacta de euros: "))

bills_and_coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]

if amount < 0:
    print("Por favor, introduce una cantidad válida (no negativa).")
else:
    for value in bills_and_coins:
        count = amount // value
        if count > 0:
            print(f"{count} billete(s)/moneda(s) de {value}€")
        amount = amount % value



