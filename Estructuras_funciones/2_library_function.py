"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones.
Recuerda que puedes usar unas dentro de otras si es necesario.

Observa bien lo que hace cada función, si las implementas en el orden adecuado,
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


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    candidate = abs(n) + 1
    if candidate < 2:
        candidate = 2

    while not is_prime(candidate):
        candidate += 1
    return candidate


def digits(n):
    n = abs(n)
    if n == 0:
        return 1
    return int(math.log10(n)) + 1


def reverse(n):
    n_abs = abs(n)
    reversed_num = 0
    while n_abs > 0:
        reversed_num = reversed_num * 10 + n_abs % 10
        n_abs //= 10

    return reversed_num if n >= 0 else -reversed_num


def is_palindromic(n):
    return abs(n) == reverse(abs(n))


def digit_n(n, pos):
    n_abs = abs(n)
    total_digits = digits(n_abs)

    if pos < 0 or pos >= total_digits:
        return -1

    desplazamientos = total_digits - pos - 1

    n_abs //= 10 ** desplazamientos

    return n_abs % 10


def digit_position(n, digit):
    n_abs = abs(n)
    temp_n = n_abs
    total_digits = digits(n_abs)

    for pos in range(total_digits):
        current_digit = digit_n(temp_n, pos)
        if current_digit == digit:
            return pos

    return -1


def remove_behind(n, count):
    n_abs = abs(n)
    for _ in range(count):
        n_abs //= 10

    return n_abs if n >= 0 else -n_abs


def remove_ahead(n, count):
    n_abs = abs(n)
    total_digits = digits(n_abs)

    if count >= total_digits:
        return 0

    potencia = 10 ** (total_digits - count)
    result_abs = n_abs % potencia

    return result_abs if n >= 0 else -result_abs


def paste_behind(n, digit):
    n_abs = abs(n)
    result_abs = n_abs * 10 + digit

    return result_abs if n >= 0 else -result_abs


def paste_ahead(n, digit):
    n_abs = abs(n)
    total_digits = digits(n_abs)
    result_abs = digit * 10 ** total_digits + n_abs

    return result_abs if n >= 0 else -result_abs


def piece_of_number(n, start, end):
    n_abs = abs(n)
    total_digits = digits(n_abs)

    n_temp = remove_ahead(n_abs, start)

    longitud_deseada = end - start + 1
    num_a_quitar_detras = digits(n_temp) - longitud_deseada

    if num_a_quitar_detras <= 0:
        result_abs = n_temp
    else:
        result_abs = remove_behind(n_temp, num_a_quitar_detras)

    return result_abs if n >= 0 else -result_abs


def concatenate(n1, n2):
    n1_abs = abs(n1)
    n2_abs = abs(n2)
    total_digits_n2 = digits(n2_abs)

    result_abs = n1_abs * 10 ** total_digits_n2 + n2_abs

    return result_abs if n1 >= 0 else -result_abs


if __name__ == "__main__":
    primo = is_prime
    siguiente_primo = next_prime
    digitos = digits
    digito_n = digit_n
    posicion_de_digito = digit_position
    pega_por_detras = paste_behind
    pega_por_delante = paste_ahead
    voltea = reverse
    es_capicua = is_palindromic
    junta_numeros = concatenate
    quita_por_detras = remove_behind
    quita_por_delante = remove_ahead
    trozo_de_numero = piece_of_number

    assert primo(2) == True
    assert primo(3) == True
    assert primo(4) == False
    assert primo(9) == False
    assert primo(19) == True
    assert primo(1) == False
    assert primo(0) == False
    assert primo(-5) == False

    assert digitos(12345) == 5
    assert digitos(45) == 2
    assert digitos(-1) == 1
    assert digitos(-12345) == 5
    assert digitos(0) == 1
    assert digitos(1234) == 4

    assert siguiente_primo(2) == 3
    assert siguiente_primo(3) == 5
    assert siguiente_primo(4) == 5
    assert siguiente_primo(9) == 11
    assert siguiente_primo(19) == 23
    assert siguiente_primo(1) == 2

    assert digito_n(12345, 0) == 1
    assert digito_n(12345, 1) == 2
    assert digito_n(-12345, 2) == 3
    assert digito_n(12345, 3) == 4
    assert digito_n(12345, 4) == 5
    assert digito_n(12345, 10) == -1

    assert posicion_de_digito(12345, 0) == -1
    assert posicion_de_digito(12345, 1) == 0
    assert posicion_de_digito(-12345, 2) == 1
    assert posicion_de_digito(12345, 3) == 2
    assert posicion_de_digito(12345, 4) == 3
    assert posicion_de_digito(12345, 5) == 4
    assert posicion_de_digito(12345, 9) == -1
    assert posicion_de_digito(55555, 5) == 0

    assert pega_por_detras(123, 9) == 1239
    assert pega_por_detras(123, 0) == 1230
    assert pega_por_detras(-123, 9) == -1239
    assert pega_por_detras(0, 5) == 5

    assert pega_por_delante(123, 9) == 9123
    assert pega_por_delante(123, 0) == 123
    assert pega_por_delante(-123, 9) == -9123
    assert pega_por_delante(5, 0) == 5

    assert voltea(1521) == 1251
    assert voltea(-1521) == -1251
    assert voltea(0) == 0
    assert voltea(8) == 8

    assert es_capicua(1521) == False
    assert es_capicua(-1521) == False
    assert es_capicua(1551) == True
    assert es_capicua(151) == True
    assert es_capicua(-151) == True
    assert es_capicua(5) == True
    assert es_capicua(0) == True

    assert junta_numeros(1521, 58) == 152158
    assert junta_numeros(-1521, 58) == -152158
    assert junta_numeros(0, 58) == 58
    assert junta_numeros(58, 0) == 580
    assert junta_numeros(58, 12345) == 5812345

    assert quita_por_detras(15215, 2) == 152
    assert quita_por_detras(-15215, 2) == -152
    assert quita_por_detras(15215, 4) == 1
    assert quita_por_detras(15215, 5) == 0
    assert quita_por_detras(15215, 0) == 15215
    assert quita_por_detras(15215, 6) == 0

    assert quita_por_delante(15215, 2) == 215
    assert quita_por_delante(-15215, 2) == -215
    assert quita_por_delante(15215, 4) == 5
    assert quita_por_delante(15215, 5) == 0
    assert quita_por_delante(15215, 0) == 15215
    assert quita_por_delante(15215, 6) == 0

    assert trozo_de_numero(15215, 1, 3) == 521
    assert trozo_de_numero(-15215, 1, 3) == -521
    assert trozo_de_numero(15215, 0, 3) == 1521
    assert trozo_de_numero(15215, 2, 4) == 215
    assert trozo_de_numero(15215, 2, 2) == 2
    assert trozo_de_numero(15215, 4, 4) == 5
    assert trozo_de_numero(15215, 5, 5) == 0

    print("\n Todas las funciones son correctas.")