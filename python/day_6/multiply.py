multiply_dict = {}
n = int(input('ingrese cantidad de multiplos a visualizar por cada número:'))
for x in range(1, 6):
    multiply_dict[x] = [(n * x) for n in range(1, n+1)]

print(multiply_dict)
