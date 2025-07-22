print(type((1, 2, 3, 4)))


a = [(x, input('Ingrese valor:')) for x in ['nombre', 'edad', 'ciudad']]
for v in a:
    print(f"{v[0]} : {v[1]}")


a, b, c = (10, 20, 30)

first = (31, 4, 5, 8, 90)
second = (6, 3, 17, 88, 91)
result = first + second
print(result)

buscar = int(input('Buscar numero:'))
principal = (4, 6, 3, 4, 4, 12, 34, 12, 5, 4, 0, 4, 9)
contador = principal.count(buscar)

print(f'en tupla {principal}')
print(f'apareció: {contador} veces')

principal = (4, 6, 3, 4, 4, 12, 34, 12, 5, 4, 0, 4, 9)
print(f'en tupla {principal}')
number = int(input('Buscar numero:'))
esta = number in principal
if esta:
    print('Está en la tupla')
else:
    print('No encontrado')

example = tuple(['lorem', 'ana', 'casa'])
print(example)
