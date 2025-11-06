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

tasa_interes_mensual = tasa_interes_anual / 100 / 12
numero_pagos = plazo_anos * 12
cuota_mensual = (importe_prestamo * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual) ** -numero_pagos)












