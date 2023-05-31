# Ir de 1 a 200 hasta alcanzar 100 (break)

import os
os.system("cls")
print("Ir de 1 a 200 hasta alcanzar 100 (break)\n")

c=0
s=0

while c<=200:
    c=c+1
    s=s+c
    print(c, end=" ")
    if s>=6000:
        break

print(f"\n\nSuma: {s} sumando {c} numeros")