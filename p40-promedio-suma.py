#Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0,
#además deberá contar cuantos números se introdujeron. El proceso debe poder repetirse hasta que el usuario lo decida.

import os 

os.system("cls")
print("Se desea calcular la suma y el promedio de una serie de numeros hasta que se ingrese 0\n")

while(True):
  
 suma  = 0
 cuenta = 0

 numero = 1
 while numero > 0:
  numero = int(input(f"Numero {cuenta+1}; "))
  if numero != 0:
   cuenta = cuenta + 1
   suma = suma + numero
  
 print(f"\nLa suma es    : {suma}")
 print(f"El promedio es: {suma/cuenta}\n")

 res = input("\nDeseas continuar (S/N) ? ")
 if res.upper()=="N":
     break 
print("\nProceso terminado...")