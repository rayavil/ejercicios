#Elaborar un programa que calcule la hipotenusa de un triángulo rectángulo

import math

#Ingresa información
print("Para calcular la hipotenusa de un triángulo rectángulo ingrese las longitudes de sus lados:\n")
lA = int(input("Longitud del lado A:"))
lB = int(input("Longitud del lado B:"))

#Calculo
hipotenusa = math.sqrt( lA * lA + lB * lB )

#Resultado
print(f"La Hipotenusa es: {hipotenusa}")