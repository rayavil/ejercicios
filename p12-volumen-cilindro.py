 #Obtener el volumen del cilindro con el radio y la altura 

import math

print("Ingresar el radio y la altura del cilindro y podrás calcular el volumen automáticamente:\n")

R = int(input("Radio:"))
A = int(input("Altura:"))
V = math.pi * (R * R) * A

print(f"El volumen del cilindro es {V} m\u00b3 ")