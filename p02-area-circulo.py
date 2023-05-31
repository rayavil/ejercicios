# Calcular el area de un circulo
import math

#Información de Entrada 
print("Calcula el area de un circulo\n")
radio = float(input("Ingresa el radio: "))

#Proceso
area = math.pi *math.pow(radio,2)
print(math.pi)

#Salida
print(f"El circulo de radio {radio} tiene un area de: {area:.2f}")