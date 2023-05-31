#Obtener el 3er ángulo de un triangulo
 
print("Para calcular el tercer ángulo se requiere conocer 2 ángulos:\n")

#Entrada de datos
anguloA = int(input("Ingresa el valor del ángulo A:"))
anguloB = int(input("Ingresa el valor del ángulo B:"))

#Calculo
tercerA = 180 - (anguloA + anguloB)

#Resultado
print(f"El valor del tercer ángulo es = {tercerA}")