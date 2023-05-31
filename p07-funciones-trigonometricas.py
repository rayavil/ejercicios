#Uso de las funciones trigonometricas en python

import math

print('Calcula las funciones trigonometricas básicas de un ángulo en radianes:\n')
angulo = int(input('Dame un angulo: '))

seno = math.sin(angulo)
cos =math.cos(angulo)
tan =math.tan(angulo)
grados =math.degrees(angulo)

salida = (f'Resumen de funciones trigonometricas\n'
f'EL seno es : {seno}\n'
f'El coseno es: {cos}\n'
f'La tangente : {tan}\n'
f'El angulo {angulo} en radianes equivale a {grados}\n')

print(salida)