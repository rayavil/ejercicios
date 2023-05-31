# Convierte una temperatura de grados Celcius a grados Farenheit y viceversa

import os
os.system("cls")

print("Convierte una temperatura de grados Celcius a grados Farenheit y viceversa:\n")
opcion= input("[C]elcius [F]arenheit ?").upper()

if opcion == "C":
    print("\nConvertir a Celcius")
    temp = float(input("Dame grados Farenheit ?"))
    res = (temp-32) * 5/9
    print(f"{temp} grados farenheit, equivale a {res} grados celcius")

else:
    print("\nConvertir a Farenheit")
    temp = float(input("Dame grados celcius ?"))
    res = (temp*9/5) + 32
    print(f"{temp} grados Celcius, equivale a {res} grados Farenheit")