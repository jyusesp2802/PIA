#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

#Autor:Jaime Yust
#Fecha: 16/10/2025

minutes  = float(input('Recibe una cantidad de minutos'))

hours = minutes //60
remaining_minutes  = minutes %60

print('Quedan',hours,'Horas y', remaining_minutes ,'minutos')