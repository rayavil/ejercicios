#Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se detiene al introducir
#0. El proceso debe poder repetirse hasta que el usuario lo decida

import os

while(True):
    
    os.system('cls')
    print('Conocer cual es el numero mayor de los numeros introducidos hasta detenerse al ingresar un 0.\n')
    print('Introduce números con enter:')
    b = True
    m = 0
    cuenta =0

    while b == True:
        num = int(input(f"Numero {cuenta+1} : "))
        cuenta = cuenta+1
        if m < num:
            m = num
        if num == 0:
            print(f'El número mayor introducido es: {m}')
            b = False
    res = input('\nDeseas continuar (S/N) ? ')
    if res.upper()=='N':
        break
print('\nProceso terminado ...')