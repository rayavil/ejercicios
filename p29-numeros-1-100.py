# Imprime números del 1 al 100

import os

os.system('cls')

print('Imprime números del 1 al 100')
n = int(input('Hasta donde?'))
m = int(input('Salto de ?'))

c = 1
while c <= n:
    print(c, end=' ')
    c = c + m

print('\n Proceso terminado')