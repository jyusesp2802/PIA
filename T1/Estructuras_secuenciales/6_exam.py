#Escribir un programa para calcular la nota final de un examen, considerando que:

#Cada respuesta correcta suma 5 puntos.
#Cada respuesta incorrecta suma -1 puntos.
#Cada respuesta en blanco suma 0 puntos.
#Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.

#Autor:Jaime Yust
#Fecha: 16/10/2025

SCORE_RIGHT = 5

print('Calculadora de nota final de examen')

correct = float(input('Respuestas correctas:'))
wrong = float(input('Respuestas incorrectas:'))
blank = float(input('Respuestas en blanco:'))

points_correct = correct * SCORE_RIGHT
points_wrong = wrong * (-1)
points_blank = blank * 0

answers = (correct + wrong + blank) * SCORE_RIGHT

preliminary_test = points_correct + points_wrong + points_blank

final_test = (preliminary_test / answers) * 10

print(f'La nota final es de:{final_test:.2f}')

