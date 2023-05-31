# Imprimer números de 1 a n o de n a 1 según lo decida el ususario
import os

while (True):
    os.system('cls')
    print('[1] números de 1 a n')
    print('[2] números de n a 1')

    op = int(input('Elige? '))
    n = int(input('Limite de n '))

    if op ==1:
        print(f'\n Imprime los números de 1 a {n}')
        for v in range(1, n+1):
            print(v, end=' ')
    elif op==2:
        print(f'\n Imprime los números de {n} a 1')
        for r in range(n, 0, -1):
            print(r, end=' ')
    else:
        print('Opción invalida')
    
    res = input('\n\n Deseas continuar (S/N)? ').upper()
    if res == 'N': break

print('\n\n Proceso terminado')