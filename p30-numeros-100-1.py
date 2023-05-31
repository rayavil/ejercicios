# Imprime números del 100 al 1

import os

os.system('cls')

print('Imprime números del 100 al 1')
n = int(input('Desde donde? '))
m = int(input('Salto de '))

c = n

while c >= 0:
    print(c, end=' ')
    c = c - m

print('\n Proceso terminado...')