# Lee los datos y envia un saludo

print("Leyendo datos y enviando un saludo\n")

#Entrada
nombre=input("Dame tu nombre: ") #lee una cadena
edad=int(input("Dame tu edad: "))
peso=float(input("Dame tu peso: "))

#Salida
print(f"{nombre} bienvenid@ a python, tu edad es {edad}, y tu peso es de {peso}")
print(type(nombre)) #muestra el dato de tipo de variable
print(type(edad))
print(type(peso))