# verificar si la suma de dos numeros es igual a un terecero

import os

os.system('cls')
print('Verifica si la suma de dos números es igual a un tercero')
print('Dame 3 números separados por espacio:\n')

n1, n2, n3 = input().split()
n1, n2, n3 = [int(n1), int (n2), int(n3)]
if n1 + n2 == n3:
    print('n1 + n2 = n3')
elif n1 + n3 == n2:
    print('n1 + n3 = n2')
elif n2 + n3 == n1:
    print('n2 + n3 = n1')
else:
    print('posiblemente son iguales')