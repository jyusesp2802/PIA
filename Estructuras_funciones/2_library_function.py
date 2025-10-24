"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones.
Recuerda que puedes usar unas dentro de otras si es necesario.

Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado,
te puedes ahorrar mucho trabajo. Por ejemplo, la función is_palindromic() resulta trivial teniendo reverse()
y la función next_prime() también es muy fácil de implementar teniendo is_prime().

Está prohibido usar funciones de conversión del número a una cadena.

is_palindromic: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
is_prime: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
next_prime: devuelve el menor primo que es mayor al número que se pasa como parámetro.
digits: devuelve el número de dígitos de un número entero.
reverse: le da la vuelta a un número.
digit_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda a derecha.
digit_position: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra, devuelve -1.
remove_behind: le quita a un número n dígitos por detrás (por la derecha).
remove_ahead: le quita a un número n dígitos por delante (por la izquierda).
paste_behind: añade un dígito a un número por detrás.
paste_ahead: añade un dígito a un número por delante.
piece_of_number: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.
concatenate: pega dos números para formar uno.
Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.

Autor: Jaime Yust
Fecha: 23/10/2025

"""

import math

def is_primo(prime_number):
    if prime_number < 2:
        return False
    for i in range(2, int(math.sqrt(prime_number)) + 1):
        if prime_number % i == 0:
            return False
    return True

def next_prime(prime_number):
    next_number = prime_number + 1
    while not is_primo(next_number):
        next_number += 1
    return next_number

def digits(number):
    abs(number)
    total_digits = 1
    while number // 10 > 0:
        total_digits += 1
        number //= 10
    return total_digits


