#Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano ( I, II, III, IV, V,
#VI, VII, VIII, IX, X). Si el número no esta en el rango solicitado que mande un mensaje de error.


import os
os.system("cls")

print("Muestra el equivalente del numero romano del 1 al 10:\n")
numero= int(input("Ingresa un numero entre 1 y 10 : "))

if numero >= 1 and numero <= 10:
    
    if numero == 1 :
        romano = "I"

    elif numero == 2:
        romano = "II"

    elif numero == 3:
        romano = "III"

    elif numero == 4:
        romano = "IV"

    elif numero == 5:
        romano = "V"

    elif numero == 6:
        romano = "VI"

    elif numero == 7:
        romano = "VII"

    elif numero == 8:
        romano = "VIII"

    elif numero == 9:
        romano = "IX"
        
    elif numero == 10:
        romano = "X"

    else:
        print("completo")
        
    print(f"\n El {romano} es el numero romano de {numero}")
else:
    print("el numero esta fuera de rango...")

