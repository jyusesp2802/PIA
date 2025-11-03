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
        self.simplify()

    def simplify(self):
        def mcd(a, b):
            while b:
                a, b = b, a % b
            return a
        common_divisor = mcd(abs(self.__numerator), abs(self.__denominator))
        self.__numerator //= common_divisor
        self.__denominator //= common_divisor
        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def sum (self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = (self.__numerator * other.denominator) + (other.numerator * self.__denominator)
        new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def difference (self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = (self.__numerator * other.denominator) - (other.numerator * self.__denominator)
        new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def multiply (self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.__numerator * other.numerator
        new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def divide (self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.__numerator * other.denominator
        new_denominator = self.__denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def equal (self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return (self.__numerator * other.denominator) == (other.numerator * self.__denominator)

    def less_than (self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return (self.__numerator * other.denominator) < (other.numerator * self.__denominator)

    def less_equal (self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return (self.__numerator * other.denominator) <= (other.numerator * self.__denominator)

    def greater_than (self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return (self.__numerator * other.denominator) > (other.numerator * self.__denominator)

    def greater_equal (self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return (self.__numerator * other.denominator) >= (other.numerator * self.__denominator)

    def not_equal (self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return (self.__numerator * other.denominator) != (other.numerator * self.__denominator)

# Pruebas de la clase Fraction
try:
    denominator1 = int(input("Introduce el denominador de la primera fracción: "))
except ValueError:
    print("Error: Por favor, introduce un número entero positivo .")
    denominator1 = int(input("Introduce el denominador de la primera fracción: "))
numerator1 = int(input("Introduce el numerador de la primera fracción: "))

try:
    denominator2 = int(input("Introduce el denominador de la segunda fracción: "))
except ValueError:
    print("Error: Por favor, introduce un número entero positivo .")
    denominator2 = int(input("Introduce el denominador de la segunda fracción: "))
numerator2 = int(input("Introduce el numerador de la segunda fracción: "))

def menu():
    print("\nMenú de operaciones con fracciones:")
    print("1. Elegir fracción")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Comparar")
    print("7. Salir")
    choice = input("Elige una opción (1-7): ")
    return choice


fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)
print("Fracción 1:", fraction1)
print("Fracción 2:", fraction2)

while True:
    choice = menu()

    if choice == '1':
        frac_choice = input("Vuelve a introducir fracción (1 o 2): ")

        if frac_choice == '1':
            try:
                denominator1 = int(input("Introduce el denominador de la primera fracción: "))
                numerator1 = int(input("Introduce el numerador de la primera fracción: "))
            except ValueError:
                print("Error: Por favor, introduce números enteros válidos.")
                continue

            if denominator1 <= 0:
                print("Error: El denominador debe ser un número positivo distinto de cero.")
                continue

            fraction1 = Fraction(numerator1, denominator1)
            print("Fracción 1 actualizada:", fraction1)

        elif frac_choice == '2':
            try:
                denominator2 = int(input("Introduce el denominador de la segunda fracción: "))
                numerator2 = int(input("Introduce el numerador de la segunda fracción: "))
            except ValueError:
                print("Error: Por favor, introduce números enteros válidos.")
                continue

            if denominator2 <= 0:
                print("Error: El denominador debe ser un número positivo distinto de cero.")
                continue

            fraction2 = Fraction(numerator2, denominator2)
            print("Fracción 2 actualizada:", fraction2)

        else:
            print("Error: Debes elegir 1 o 2.")
            continue

    elif choice == '2':
        result = fraction1.sum(fraction2)
        print("Resultado de la suma:", result)

    elif choice == '3':
        result = fraction1.difference(fraction2)
        print("Resultado de la resta de :", result)

    elif choice == '4':
        result = fraction1.multiply(fraction2)
        print("Resultado de la multiplicación:", result)

    elif choice == '5':
        result = fraction1.divide(fraction2)
        print("Resultado de la división:", result)

    elif choice == '6':
        print("Fracción 1 == Fracción 2:", fraction1.equal(fraction2))
        print("Fracción 1 < Fracción 2:", fraction1.less_than(fraction2))
        print("Fracción 1 <= Fracción 2:", fraction1.less_equal(fraction2))
        print("Fracción 1 > Fracción 2:", fraction1.greater_than(fraction2))
        print("Fracción 1 >= Fracción 2:", fraction1.greater_equal(fraction2))
        print("Fracción 1 != Fracción 2:", fraction1.not_equal(fraction2))

    elif choice == '7':
        print("Programa terminado")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")
