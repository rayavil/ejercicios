#Dados tres números enteros, verificar cual es el mayor.

print('Ingresa tres numero para verificar cual es el mayor: \n')

numero1 = int(input("Primer numero\n"))
numero2 = int(input("Segundo numero\n"))
numero3 = int(input("Tercer numero\n"))

if(numero1 > numero2 and numero1 > numero3):
 print(f"El numero mayor es {numero1}")
else:
 if(numero2 > numero1 and numero2 > numero3):
  print(f"El numero mayor es {numero2}")
 else:
  print(f"El numero mayor es {numero3}")