"""
Examen T1 Python
Fecha: 27/11/2025
Autor: Jaime Yust Espinosa

"""

RETENCIONES = 0.15
VALOR_TRIENIO = 30

from typeguard import typechecked

@typechecked
class Nomina:
    total_nominas = 0

    def __init__ (self, nombre:str, salario_base:int, trienios:int, valor_trienio = VALOR_TRIENIO, retenciones = RETENCIONES ):
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")
        if salario_base >= 0:
            raise ValueError("El salario base es >= que 0")
        if valor_trienio <= 0:
            raise ValueError("Los trienios tienen que ser <= que 0")

        self.__nombre_empleado = nombre
        self.__salario_base = salario_base
        self.__trienios = trienios
        self.__valor_trienio = valor_trienio
        self._retenciones = retenciones
        Nomina.total_nominas += 1

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












