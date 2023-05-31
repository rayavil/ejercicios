#Imprime numeros del 1 al 200 de 10 en 10 (continue)

import os 
os.system("cls")

print("Imprimir numeros del 1 al 200 de 10 en 10 (continue):\n")

c=1
while c <= 200:
    c= c + 1
    if c % 10 != 0:
        continue
    print(c, end= " ")