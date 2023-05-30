# Nombres y edades
import os; os.system('clear') 
grupo = []

print('Introduce nombres y edades (nombre vacio para terminar)') 
while True: 
    datos= {} 
    nombre = input('Escribe el nombre ? ') 
    if nombre!='': 
        datos['nombre']=nombre 
        datos['edad']=int(input('Edad ? ')) 
        datos['sexo']=input('Sexo h/m ? ')
        datos['sueldo']=float(input('Sueldo ? ')) 
        grupo.append(datos)
    else: 
        break 
print(f'El diccionario de datos creado: \n{len(grupo)}-{grupo}\n') 


print('\nDatos en forma de Tabla:\n') 
for k in grupo[0].keys(): # titulos de la tabla 
    print(f'{k}\t', end='') 
print('\r') 

for alumno in grupo: # para cada alumno 
    for v in alumno.values(): # imprime sus valores 
        print(f'{v}\t', end='') 
    print('\r')


print('\nListado y promedio de edades:') 
se=0
ss=0 
pe=0
ps=0
sm=0
sh=0

for alumno in grupo:
    if alumno ['sexo'] =='h':
        sh = sh+1
    if alumno ['sexo'] =='m':
        sm = sm+1
    se=se+alumno['edad']
    ss=ss+alumno['sueldo']
pe=se/len(grupo)
ps=ss/len(grupo)

print(f'Empleados: {len(grupo)}')
print(f'Mujeres:   {sm}')
print(f'Hombres:   {sh}')

print(f'Edad: Suma: {se} promedio: {pe}')
print(f'Sueldo Suma: {ss} promedio: {ps}')