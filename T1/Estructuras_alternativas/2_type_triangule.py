#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

#Autor:Jaime Yust
#Fecha: 16/10/2025.

print("Programa para determinar el tipo de triángulo según sus lados.")

side_a = float(input("Introduce la longitud del lado A del triángulo: "))
side_b = float(input("Introduce la longitud del lado B del triángulo: "))
side_c = float(input("Introduce la longitud del lado C del triángulo: "))

if (side_a**2 + side_b**2 == side_c**2) or (side_a**2 + side_c**2 == side_b**2) or (side_b**2 + side_c**2 == side_a**2):
    print("El triángulo es rectángulo.")
if side_a == side_b == side_c:
    print("El triángulo es equilátero.")
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
