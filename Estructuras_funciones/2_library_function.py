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

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

def digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def reverse(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

def is_palindromic(n):
    return n == reverse(n)

def digit_n(n, pos):
    total_digits = digits(n)
    if pos < 0 or pos >= total_digits:
        return -1
    for _ in range(total_digits - pos - 1):
        n //= 10
    return n % 10

def digit_position(n, digit):
    pos = 0
    total_digits = digits(n)
    while n > 0:
        if n // 10**(total_digits - 1) == digit:
            return pos
        n %= 10**(total_digits - 1)
        total_digits -= 1
        pos += 1
    return -1

def remove_behind(n, count):
    for _ in range(count):
        n //= 10
    return n

def remove_ahead(n, count):
    total_digits = digits(n)
    for _ in range(count):
        n %= 10**(total_digits - 1)
        total_digits -= 1
    return n
def paste_behind(n, digit):
    return n * 10 + digit

def paste_ahead(n, digit):
    total_digits = digits(n)
    return digit * 10**total_digits + n

def piece_of_number(n, start, end):
    total_digits = digits(n)
    for _ in range(total_digits - end - 1):
        n //= 10
    piece = n % 10**(end - start + 1)
    return piece // 10**start

def concatenate(n1, n2):
    total_digits_n2 = digits(n2)
    return n1 * 10**total_digits_n2 + n2

