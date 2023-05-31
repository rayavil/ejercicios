#Imprimir numeros de 100 a 1

import os
os.system ("Cls")

n = int(input("Desde donde: "))
s = int(input("Paso:"))

for num in range (n, 0,-s):
    print (num,end= " ")