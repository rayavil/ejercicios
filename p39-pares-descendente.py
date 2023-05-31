#Se desea imprimir los números pares desde 100 hasta el número que el usuario decida (n), además deberá
#imprimirse la suma de esos números pares. El proceso debe poder repetirse hasta que el usuario lo decida

import os

os.system("cls")

while(True):
    
    limite= int(input("\nIndica el limite inferior a 100 paraa sumar los pares: "))
    contador =100
    suma = 0

    while contador >= limite:
        
        if contador % 2 == 0:
            print(contador, end=" ")        
            suma = suma + contador
            contador = contador-2
        
    print(f"\n\nLa suma de los números pares es: {suma} ")

    res=input('\nDeseas Continuar (S/N): ') 
    if res.upper()=='N':
        break

print("\nProceso terminado...")