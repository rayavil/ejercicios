#Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado. La
#Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5.

import os
os.system("cls")

print("El ingreso a la Universidad Kitty se realiza en base a su sexo, su edad y sus calificaciones\n")
nombre = str(input("Cual es tu nombre ? "))

sexo = str(input(f"Hola {nombre}, ahora ingresa tu sexo marcando [F]emenino y [M]asculino:\n")).upper()
edad= int(input("Ingresa tu edad:"))

nota1 = int(input("Calificación 1: "))
nota2 = int(input("Calificación 2: "))
nota3 = int(input("Calificación 3: "))

promedio = (nota1 + nota2 + nota3) /3

if sexo == "F" and edad > 21:
       
       if promedio >=8 and promedio <=9.5:
        print(f"{nombre}, bienvenida a la Universidad Kitty")

else:
    print("Lo sentimos, esta universidad es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5")

print("\n Proceso terminado")