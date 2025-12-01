"""
Examen T1 Python
Fecha: 27/11/2025
Autor: Jaime Yust Espinosa

"""

from __future__ import annotations
from typeguard import typechecked

@typechecked
class Nomina:
    total_nominas = 0

    def __init__ (self, nombre: str, salario_base: float, valor_trienio: float = 30.0 , retenciones: float = 0.15 ):
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")
        if salario_base >= 0:
            raise ValueError("El salario base es >= que 0")
        if valor_trienio <= 0:
            raise ValueError("Los trienios tienen que ser <= que 0")

        self.__nombre_empleado = nombre
        self.__salario_base = salario_base
        self._trienios = 0
        self.__valor_trienio = valor_trienio
        self.retenciones = retenciones
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

    @retenciones.setter
    def retenciones(self, value: float):
        if value < 0 or value >= 0.5:
            raise ValueError("Deben estar entre 0 y 0.5")
        self.__retenciones = value

    @property
    def salario_bruto(self):
        bruto =elf.__salario_base + self.__trienios * self.__valor_trienio
        return bruto

    @property
    def salario_neto(self):
        neto = self.salario_bruto * (1-self.__retenciones)
        return neto

    def incrementar_trienio(self):
        self.__trienios += 1


    def modificar_salario(self, porcentaje:float):
       if porcentaje <= -1 or porcentaje > 1:
           raise ValueError("El porcentaje deber estar entre -1 y 1 ")
       self.__salario_base = porcentaje * self.__salario_base

    def __str__(self):
        str_ = (f"Su nombre es {self.__nombre_empleado}, "
                f"su salario base es {self.__salario_base}, "
                f"sus trienios son {self.__trienios} x {self.__valor_trienio} €, "
                f"su salario total antes de las retenciones es {self.salario_bruto()} de €/mes,"
                f"se le aplican {self.__retenciones} retenciones,"
                f"tiene un salario neto de {self.salario_neto()} €/mes")
        return str_

    def __eq__ (self, other: Nomina):
        return self.salario_neto() == other.salario_neto()

    def __lt__ (self, other: Nomina):
        return self.salario_neto() < other.salario_neto()

    def __gt__(self, other: Nomina):
        return self.salario_neto() > other.salario_neto()

    def __ge__ (self, other: Nomina):
        return self == other or self > other

    def __le__ (self, other: Nomina):
        return self == other or self < other

    def __ne__ (self, other: Nomina):
        return not (self == other)

    def __del__ (self, other: Nomina):
        Nomina.total_nominas -= 1


    class NominaA1(Nomina):

        def __init__(self, nombre, retenciones):
            super().__init__(nombre, salario_base=2000, valor_trienio=50, )




















