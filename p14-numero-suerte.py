#Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte. 
#Mostrar los dígitos individuales y el número de la suerte.

import math 

print('Para conocer tu numero de la suerte ingresa tu año de nacimiento:') 

anio = str(input('Año de nacimiento: ')) 

# inicializando subcadena
A = 1
# crear una lista de resultados
result = []
suma = 0
for i in range(0, len(anio), A):
    # convertir a entero, despues del proceso de separacion
    suma = suma + int(anio[i : i + A])
    result.append(int(anio[i : i + A]))

print(f'Tu numero de la suerte es: {suma}' )
print("Los digitos individuales son : " + str(result))

