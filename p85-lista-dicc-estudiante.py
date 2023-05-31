grupo = [
    {"nombre": "Carlos","edad":45,"carrera":"sistemas","promedio":9.0},
    {"nombre": "Rocio","edad":35,"carrera":"contabilidad","promedio":10.0},
]

print(grupo, len(grupo))

while True:
    datos = {}
    nombre = input("\nnombre: ")
    if nombre ==" ":
        break
    else:
        datos["nombre"] = nombre
        datos["edad"] = int(input("Dame la edad:"))
        datos["carrera"] = input("Dame la carrera:")
        datos["promedio"] = float(input("Dame el promedio:"))
        grupo.append(datos)

print(grupo, len(grupo))

print("\nDatos en forma de tabla")
for k in grupo[0].keys():
    print(f"{k}\t", end =" ")
print("\r")

for auto in grupo:
    for v in auto.values():
        print(f"{v}\t",  end=" ")
    print("\r")

#Calcular suma de edades
s = 0
sp = 0
for alumno in grupo:
    s = s + alumno["edad"]
    sp = sp + alumno["promedio"]
p = s/len(grupo)
pp = sp/len(grupo)

print("\nResumen:")
print(f"Edad:      suma {s}, promedio {p}")
print(f"Promedio:  suma {sp}, promedio {pp}")