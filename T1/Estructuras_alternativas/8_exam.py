#Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen, proporcione la calificación cualitativa correspondiente al número dado.
#La calificación cualitativa será una de las siguientes:
# «Suspenso» (nota menor que 5)
# «Aprobado» (nota mayor o igual que 5, pero menor que 7)
# «Notable» (nota mayor o igual que 7, pero menor que 9)
# «Sobresaliente» (nota mayor o igual que 9, pero menor que 10)
# «Matrícula de Honor» (nota 10).

#Autor:Jaime Yust
#Fecha: 16/10/2025

grade = float(input("Introduce la calificación numérica del examen (0-10): "))
if grade < 0 or grade > 10:
    print("Error: La calificación debe estar entre 0 y 10.")
elif grade < 5:
    print("Suspenso")
elif grade < 7:
    print("Aprobado")
elif grade < 9:
    print("Notable")
elif grade < 10:
    print("Sobresaliente")
else:
    print("Matrícula de Honor")
