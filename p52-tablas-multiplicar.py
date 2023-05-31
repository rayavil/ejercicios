#Imprime las tablas del 1 a n, del 1 hasta n.

import os
os.system("cls")


n = int(input("Que tabla quieres?"))
m = int(input("Hasta donde? "))

for i in range (1,n+1):
    print(f"\nTabla del {i}")
    for j in range (1,m+1):
        print(f"   {i} x {j} = {i*j}")