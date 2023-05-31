
import os;os.system('cls')

import random #Sirve para las listas aleatorias.

a=[]
b=[]
c=[]

print('Generando listas de numeros aleatorios...')

for n in range (10):
    a.append(random.randint(5,10)) 
    b.append(random.randint(5,10)) #Se hace la aleatorizacion de 10 numeros del 5 al 10 y se van guardando en b.

print(a)
print(b)

for n in range (10):
    a[n] = a[n] * a[n]  #Se elevo al cuadrado de cada lista 
    b[n] = b[n] * b[n]
print('\nNumeros elevados al cuadrado')
print(a)
print(b)

for n in range (10):
    c.append(a[n] + b[n])
print('\nTercer lista') #Suma de las listas anteriores elevadas al cuadrado
print(c)