# Calcular el promedio de 3 calificaciones separadas por espacios

print("Calculando el promedio de 3 calificaciones:\n")
print ("Dame 3 calificaciones separadas por espacio:")

c1, c2, c3 =input().split()
c1, c2, c3 =[float(c1),float(c2),float(c3)]

suma = (c1 + c2 + c3 ) 
prom = suma / 3

print(f"El promedio de: {c1} {c2} {c3} es {prom} y la suma es {suma}")