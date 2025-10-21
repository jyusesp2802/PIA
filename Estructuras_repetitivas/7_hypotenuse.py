"""
Crea un programa que nos permita calcular la cuota de una hipoteca y
su tabla de amortización después de que se pida al usuario/a:

Importe del préstamo.
La tasa de interés anual.
Y el plazo de pago en años.

Autor:Jaime Yust
Fecha: 16/10/2025
"""

print('Calculadora de hipoteca y tabla de amortización')

importe_prestamo = float(input("Introduce el importe del préstamo: "))
tasa_interes_anual = float(input("Introduce la tasa de interés anual (en %): "))
plazo_anos = int(input("Introduce el plazo de pago en años: "))

tasa_interes_mensual = tasa_interes_anual / 100 / 12 #Convertir la tasa anual a mensual
numero_pagos = plazo_anos * 12 #Número total de pagos mensuales
cuota_mensual = (importe_prestamo * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual) ** -numero_pagos) #Fórmula de la cuota mensual

print(f"\nLa cuota mensual de la hipoteca es: {cuota_mensual:.2f}€\n")
print("Tabla de amortización:")
print("Pago\tInterés Principal\tSaldo Restante\t")

while importe_prestamo > 0:
    interes_mensual = importe_prestamo * tasa_interes_mensual
    principal_mensual = cuota_mensual - interes_mensual
    importe_prestamo -= principal_mensual
    if importe_prestamo < 0:
        principal_mensual += importe_prestamo
        importe_prestamo = 0
    print(f"{numero_pagos}\t{interes_mensual:.2f}\t\t{principal_mensual:.2f}\t\t{importe_prestamo:.2f}")
    numero_pagos -= 1










