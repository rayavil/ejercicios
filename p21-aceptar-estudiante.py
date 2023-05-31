#Aceptar un estudiante en base a su edad y sus calificaicones

import os
os.system("cls")

print("Aceptar un estudiante en base a su edad y sus calificaicones\n")
nombre = input("Dame tu nombre: ")
edad   = int( input("Dame tu edad: "))

if edad < 18 :
    print("No acpetamos menores de edad...")
else:
    print("Dame dos calificaciones separadas por enter: ")
    c1,c2 = int(input()), int(input())
    if c1<8 or c2<8:
        print("No aceptamos calificaciones menores a 8")
    else:
        print(f"{nombre} bienvenido(a) a la universidad, tu edad es {edad} y tus calificaciones {c1} y {c2} lo permiten")


print("\n Proceso terminado")