#Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos, considerando que:
#• 1 día tiene 24 horas,
#• 1 hora tiene 60 minutos,
#• 1 minuto tiene 60 segundos.

print("Conversor de horas en días, minutos y segundos:\n")

#Entrada de datos
hrs= int(input ("Ingresa la cantidad de horas:"))

dias = hrs / 24
min  = hrs * 60
seg = min * 60

print(hrs, f' Horas corresponden a {dias} días, {min} minutos y {seg} segundos')
