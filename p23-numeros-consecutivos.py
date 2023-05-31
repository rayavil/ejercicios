#Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, si no lo son
#(1,4,6) mandar mensaje de error.

import os

os.system('cls')
print('Dame tres números enteros separados con un espacio: \n')
numero1 = int(input("Primer numero:"))
numero2 = int(input("Segundo numero:"))
numero3 = int(input("Tercer numero:"))

if numero1 + 1 == numero2:
    if numero2 + 1 == numero3:
        print(f'Los numeros {numero1}, {numero2} y {numero3}  son consecutivos.')
    else:
        print('Error, no son consecutivos.')
else:
    print('Error, no son consecutivos.')

print('\nProceso terminado')