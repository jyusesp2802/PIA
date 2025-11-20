#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
#Escribir un programa que determine la hora de llegada a la ciudad B.

#Autor:Jaime Yust
#Fecha: 16/10/2025

HH = float(input('Hora de salida: '))
MM = float(input('Minutos de salida: '))
SS = float(input('Segundos de salida: '))

T = float(input('Tiempo en llegar a la otra ciudad en sgundos: '))

departure_seconds = HH * 3600 + MM * 60 + SS

arrival = departure_seconds + T

arrival_hour = arrival // 3600
arrival_minutes = (arrival % 3600) // 60
arrival_seconds = arrival % 60

print('Llego a las', arrival_hour, 'h', arrival_minutes, 'm', arrival_seconds, 's')

