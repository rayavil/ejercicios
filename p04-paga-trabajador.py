# Calcular la paga total de un trabajador

print ("Calcular la paga total de un trabajador:\n")
nombre = input("Dame tu nombre: ")
horas = int(input("horas trabajadas: "))
paga = float(input ("Paga por hora: "))

tasa = 0.3

pagabruta= horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto 

print("\nResumen de pagos:\n")
print (f"El trabajador {nombre} trabajo {horas} horas con una paga de {paga} pesos")
print(f"paga bruta:{pagabruta}")
print(f"impuesto:{impuesto}")
print(f"paganeta:{paganeta}")