"""
 Implementa una clase llamada Nomina que cumpla los siguientes requisitos:
 Atributos
 a) Atributo de clase
 • total_nominas: contador del número total de nóminas creadas (tanto de esta clase como
de sus subclases).
 b) Atributos de instancia
 • __nombre_empleado
 • no puede estar vacío
 • no cambia
 • __salario_base
 • tiene que ser >0
 • solo cambia con un método (no hay setter)
 • __trienios (número de trienios del empleado)
 • tiene que ser >=0
 • solo cambia con un método (no hay setter)
 • __valor_trienio (importe económico de cada trienio)
 • tiene que ser >0
 • no cambia
 • __retenciones: porcentaje total de retenciones aplicadas.
 • Tiene que ser >=0 y <0.5
 • puede cambiar
 Constructor
 Debe recibir:
 nombre_empleado, salario_base, retenciones (por defecto 0.15) y valor_trienio
(por defecto 30).
 Cada vez que se cree un objeto, debe incrementarse total_nominas.
Cada vez que se destruya un objeto, debe decrementarse total_nominas.
 Propiedades
 En función de las características de los atributos de instancia crea las propiedades de lectura (getter)
y/o escritura (setter).
 Métodos requeridos
 1. Método público calcular_neto():
 Calcula el salario neto aplicando:
 • Salario total = salario base + (trienios × valor_trienio)
 • Neto = salario total × (1 – retenciones/100)
 Debe devolver el salario neto calculado.
 2. Método público incrementar_trienio():
 Debe incrementar en 1 el total de trienios.
 3. Método público modificar_salario(porcentaje):
 Debe modificar el salario base en el porcentaje (positivo o negativo) que indica el
parámetro. El salario base final no puede ser negativo.
 4. Método mágico __str__():
 Devuelve un texto con:
 • nombre del empleado
 • salario base
 • trienios y su valor
 • salario total antes de retenciones
 • retenciones aplicadas
 • salario neto final (usando el método privado)
 5. Métodos mágicos de sobrecarga de operadores relaciones sobre el neto de la nómina.

Fecha: 27/11/2025
Autor: Jaime Yust Espinosa

"""

RETENCIONES = 0.15
VALOR_TRIENIO = 30



from typeguard import typechecked

@typechecked
class Nomina:

    def __init__ (self, nombre:str, salario_base:int, trienios:int, valor_trienio = VALOR_TRIENIO, retenciones = RETENCIONES ):
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")
        if salario_base > 0:
            raise ValueError("El salario base es > que 0")
        if trienios >= 0:
            raise ValueError("Los trienios tienen que ser >= que 0")
        if (retenciones < 0) and (retenciones > 0.5):
            raise ValueError("Las retenciones deben estar entre 0 y 0.5")

        self.__nombre_empleado = nombre
        self.__salario_base = salario_base
        self.__trienios = trienios
        self.__valor_trienio = valor_trienio
        self.__retenciones = retenciones

    @property
    def nombre(self):
        return self.__nombre_empleado

    @property
    def salario_base(self):
        return self.__salario_base

    @property
    def valor_trienio(self):
        return self.__valor_trienio

    @property
    def retenciones(self):
        return self.__retenciones

    def calcular_neto(self, neto):
        salario_total = self.__salario_base + (self.__trienios * self.__valor_trienio)
        neto = salario_total * (1 - self.__retenciones)
        return f"El salario neto es {neto}"

    def incrementar_trienio(self):
        self.__trienios =+ 1


    def modificar_salario(self, porcentaje:float):
        porcentaje = input("Que porcentaje modificamos la nomina")
        self.__salario_base = self.__salario_base + self.__salario_base * porcentaje
        return

    def __str__(self):
        _str= (f"Su nombre es {self.__nombre_empleado}, "
                f"su salario base es {self.__salario_base}, "
                f"sus trienios son {self.__trienios} y tienen un valor de {self.__valor_trienio} €, "
                f"su salario total antes de las retenciones es {"salario_total"} de €/mes,"
                f"se le aplican {self.__retenciones} retenciones,"
                f"tiene un salario neto de {"neto"} €/mes")

        return _str



class NominaA1(Nomina):

    def __init__(self, nombre, retenciones):
        super().__init__(nombre, salario_base = 2000,  valor_trienio = 50,  )












