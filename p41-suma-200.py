#Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, luego mostrar
#cuantos números fueron introducidos y la suma de estos. El proceso debe poder repetirse hasta que el usuario lo decida.

import os 


os.system("cls")
print("Ingresa una secuencia de numeros, el proceso terminará cuando la suma sea mayor a 200")

while(True):
  
  suma = 0
  cuenta = 0
  
  
  while (True):
   num = int(input(f"Numero {cuenta+1} : "))
   if num <= 200:
     suma = suma + num
     cuenta = cuenta + 1
   if suma >= 200 :
     break

  print (f"\nSe introdujeron {cuenta} numeros ")
  print(f"\nLa suma de los numeros es: {suma}")

  res = input("\nDeseas continuar (S/N) ? ")
  if res.upper()=="N":
   break 
print("\nProceso terminado...")