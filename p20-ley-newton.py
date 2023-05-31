# Calcula la ley de Newton (fuerza, masa, aceleración)

import os

os.system('cls')
print('Calcula la segunda ley de Newton (fuerza, masa, aceleración\n:)')
print('[F]uerza      (f = m * a)')
print('[M]asa        (m = f / a)')
print('[A]celeración (a = f/ m)')

op = input('Elige Opción ?').upper()

if op == 'F':
    print('\n Calculando la Fuerza...')
    m = int(input('Dame la masa? \n'))
    a = int(input('Dame la aceleración\n ?'))
    f = m * a
    print(f'La fuerza es: {f}')
elif op == 'M':
    print('\n Calculando la masa...')
    f = int(input('Dame la fuerza?\n'))
    a = int(input('Dame la aceleración? \n'))
    m = f/a
    print(f'La masa es {m}')
elif op == 'A':
    print('Calculando la Aceleración')
    f = int(input('Dame la fuerza:\n?'))
    m = int(input('Dame la masa?\n'))
    a = f / m
    print( f'La Aceleración es {a}')
else:
    print('Opción invalida')
    
print('Proceso terminado')