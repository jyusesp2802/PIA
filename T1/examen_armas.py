
from typeguard import typechecked
import math
MAX_HEALTH = 100
@typechecked
class Armas :

    def __init__(self, nombre: str, daño_base: int, durabilidad:int ):
        if nombre == "":
            raise ValueError ("El nombre esta vacío")
        if daño_base <= 0 :
            raise ValueError ("El daño base tiene que ser mayor que 0")
        if durabilidad <= 0:
            raise ValueError ("La durabilidad tiene que ser mayor que 0")

        self.__nombre = nombre
        self.__daño_base = daño_base
        self.__durabilidad = durabilidad

    @property
    def name(self):
        return self.__nombre

    @property
    def damage(self):
        if self.__durabilidad == 0:
            return 0
        return self.__daño_base

    @property
    def durability(self):
        return self.__durabilidad

    def use(self):
        damage = self.damage
        if self.__durabilidad > 0:
            self.__durabilidad -= 1
        return damage

    def __str__(self):
        return f"Arma: {self.name}, daño base: {self.damage}, durabilidad: {self.durability}"


@typechecked
class Guerrero:

    def __init__(self, name: str, health: int, weapon: Armas):
        if name == "":
            raise ValueError("El nombre no puede estar vacío")
        if health <= 0 or health > MAX_HEALTH:
            raise ValueError(f"La vida tiene que ser mayor que 0 y menor o igual que {MAX_HEALTH}")

        self.__name = name
        self.__health = health
        self.__weapon = weapon

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def weapon(self):
        return self.__weapon
    @weapon.setter
    def weapon(self, value: Armas):
        self.__weapon = value

    def __str__(self):
        return f"Guerrero: {self.__name} - Vida: {self.__health} - Arma: {self.__weapon.name}"

    def __eq__(self, other: Guerrero):
        return self.__name == other.__name

    def __ne__(self, other: Guerrero):
        return not (self == other)

    def cure(self, health: int):
        if self.__health <= 0:
            raise ValueError("La vida tiene que ser mayor que 0")
        self.__health = min(self.__health + health, MAX_HEALTH)

    def attack(self, other: Guerrero):
        if self.__health <= 0:
            raise ValueError("No se puede atacar si la vida no es mayor que 0")
        damage = self.__weapon.use()
        other.__health = max(0, other.__health - damage)
