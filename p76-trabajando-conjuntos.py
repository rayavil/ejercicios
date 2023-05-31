municipios = {'Zacatecas', 'Guadalupe', 'Fresnillo', 'Fresnillo'}
print(municipios)
print(len(municipios))
print(type(municipios), '\n')

for m in municipios:
    print('Tu vives en ',m,'\n')

print('Zacatecas' in municipios)

municipios.add('Teul')
print(municipios, len(municipios), '\n')

otros = {'Luis Moya', 'Ojocaliente', 'Tepetongo'}
municipios.update(otros)
print(municipios, len(municipios), '\n')

municipios.remove('Ojocaliente')
print(municipios)

municipios.clear()
print(f'Eliminar con Clear() : \n{municipios}\n')
print(municipios)