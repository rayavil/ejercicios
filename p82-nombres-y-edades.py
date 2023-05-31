datos = { }

while True:
    nombre = input("nombre ? ")
    if nombre!="":
        datos[nombre] = int(input("dame la edad ?"))
    else:
        break

print(datos, len(datos))

s = 0
for n,e in datos.items():
    print(f"{n:<20} - {e:2}")
    s =s+e
    
print()
print(s)
print(s/len(datos))