
"""
En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos),
pero no nos gustan, vamos a hacer una nueva que se llamará Duration y será inmutable. Debe permitir:

Crear duraciones de tiempos.
Ejemplo: t = Duration(10,20,56)
Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
Si no indico la hora, minuto o segundo estos valores son cero:
Duration() --> (0, 0, 0)
Duration(34) --> (34, 0, 0)
Duration(34, 15) --> (34, 15, 0)
Duration(34, 61) --> (35, 1, 0)
Las duraciones de tiempo se pueden comparar.
A las duraciones de tiempo les puedo sumar y restar segundos.
Las duraciones de tiempo se pueden sumar y restar.

Autor: Jaime Yust
Fecha: 03/11/2025
"""

class duration :

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.normalize()

    def normalize(self):
        total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        self.__hours = total_seconds // 3600
        self.__minutes = (total_seconds % 3600) // 60
        self.__seconds = total_seconds % 60

    def __str__(self):
        return f"{self.hours}h {self.minutes}m {self.seconds}s"

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    def total_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    def sum (self, other):
        total = self.total_seconds() + other.total_seconds()
        return duration(0, 0, total)

    def difference (self, other):
        total = abs(self.total_seconds() - other.total_seconds())
        return duration(0, 0, total)


# Pedir duraciones al usuario

def pedir_duracion(n):
    while True:
        try:
            h = int(input(f"Horas {n} duración: "))
            m = int(input(f"Minutos {n} duración: "))
            s = int(input(f"Segundos {n} duración: "))

            # Validación solo para negativos
            if h < 0 or m < 0 or s < 0:
                print("No se permiten valores negativos.\n")
                continue

            return h, m, s
        except ValueError:
            print("Por favor, introduce solo números enteros válidos.\n")

# Uso del programa
h1, m1, s1 = pedir_duracion("primera")
h2, m2, s2 = pedir_duracion("segunda")

print(f"\nPrimera duración: {h1:02d}:{m1:02d}:{s1:02d}")
print(f"Segunda duración: {h2:02d}:{m2:02d}:{s2:02d}")



def menu():
    print("1. Sumar duraciones")
    print("2. Restar duraciones")
    print("3. Salir")
    choice = input("Opción: ")
    return choice

while True:
    choice = menu()
    if choice == '1':
        print("Primera duración:")
        d1 = duration(h1, m1, s1)
        print("Segunda duración:")
        d2 = duration(h2, m2, s2)
        result = d1.sum(d2)
        print("Resultado de la suma:", result)
    elif choice == '2':
        print("Primera duración:")
        d1 = duration(h1, m1, s1)
        print("Segunda duración:")
        d2 = duration(h2, m2, s2)
        result = d1.difference(d2)
        print("Resultado de la resta:", result)
    elif choice == '3':
        break
    else:
        print("Opción no válida.")


