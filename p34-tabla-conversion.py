#  Imprimir una tabla de conversion de peso a dolar

import os
while(True):
    
    os.system("cls")
    tc= 18.00
    
    pi= float(input("valor inicial: "))
    pf= float(input("valor final:  " ))

    c= pi
            
    print("\nPesos\tDolar")
    print ("-"*15)
    
    while c<=pf:
        print(f"{c}\t{c/tc:.4f}")
        c+=1

    print ("-"*15)

    res=input("\nDeseas continuar (S/N)? ")
    if res.upper()=='N':
        break