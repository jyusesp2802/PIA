"""Crea una clase, y pruébala, que modele fracciones. Debe permitir:

Crear fracciones indicando numerador y denominador.
 Ejemplo: f = Fraction(2, 3)
Ojo!!! No se puede tener un denominador cero.
Las fracciones pueden operar entre sí.
Sumar, multiplicar, dividir, restar.
Ojo!!! esto se puede hacer: f + 1, 5 * f
Las fracciones se pueden comparar.
==, <, <=, >, >=, !=
Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
Ojo!!! esto se puede hacer 1 < 1/2

Autor: Jaime Yust
Fecha: 03/11/2025

"""

class Fraction :

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.__numerator = numerator
        self.__denominator = denominator
        self._reduce()





