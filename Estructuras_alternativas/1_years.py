#Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad.
#En tal caso, hazlo saber con un mensaje adecuado.

#Autor:Jaime Yust
#Fecha: 16/10/2025
years_person1 = int(input("Introduce la edad de la primera persona: "))
years_person2 = int(input("Introduce la edad de la segunda persona: "))

if years_person1 < years_person2:
    print("La primera persona es más joven.")
elif years_person1 > years_person2:
    print("La segunda persona es más joven.")
else:
    print("Ambas personas tienen la misma edad.")