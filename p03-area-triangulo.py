# Calcular el area de un triangulo

print('Calculando el area de un triangulo:\n')
print('Dame la base y la altura separados por un Enter')
base, altura = int(input()), int(input()) #Aqui se leen dos datos en una sola linea, hay que dar enter entre cada linea

area = base * altura / 2

print(f'El triangulo de base {base} y altura {altura} tiene un area de {area}')