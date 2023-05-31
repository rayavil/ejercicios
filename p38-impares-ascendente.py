#Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n),
#además deberá imprimirse la suma de esos números impares. El proceso debe poder repetirse hasta que el
#usuario lo decida.

import os 

os.system("cls")
print("Imprime la suma de los numeros impares de forma ascendente:\n")

while(True):

  limite = (int(input("Hasta que numero se deben imprimir:")))
  contador = 0 
  suma = 0

  while contador < limite:
    contador = contador + 1

    if (contador % 2) != 0:
     print(contador, end = " ")
     suma = suma + contador

    if contador >= limite:
        print (f"\nLa suma de los numeros es: {suma}")

  res = input("\nDeseas continuar (S/N) ? ")
  if res.upper()=="N":
     break

print("\nProceso terminado...")