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

from __future__ import annotations
import math
from typeguard import typechecked

@typechecked
class Fraction :

    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        mcd = math.gcd(num, den)
        self.__num = num // mcd
        self.__den = den // mcd

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    def __str__(self):
        return f"{self.__num}/{self.__den}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__num, self.__den})"

    def result(self):
        return self.__num / self.__den





