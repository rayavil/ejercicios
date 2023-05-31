#Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 1 es domingo,
#2 es lunes y así hasta 7 es viernes. Si el número no está en el rango especificado, mostrar un mensaje de error
import os
os.system("cls")

print("Para conocer que día de la semana es ingresa un numero del 1 al 7:\n")
dia= int(input("Ingresa un número entre 1 y 7 : "))

if dia >= 1 and dia <= 7:
   
    if dia == 1 :
        print("El dia de la semana es Domingo")
    elif dia == 2:
        print("El dia de la semana es Lunes")
    elif dia == 3:
        print("El dia de la semana es Martes")
    elif dia == 4:
        print("El dia de la semana es Miercoles")
    elif dia == 5:
        print("El dia de la semana es Jueves")
    elif dia == 6:
        print("El dia de la semana es Viernes")
    elif dia == 7:
        print("El dia de la semana es Sabado")

else:
    print("El día seleccionado no está entre 1 y 7.")

