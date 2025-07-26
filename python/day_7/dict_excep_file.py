
try:
    with open('numbers.txt', 'r', encoding='utf8') as numbers:
        numeros = []
        for numero in numbers:
            try:
                numeros.append(int(numero))
            except ValueError:
                print(f'Valor no válido: {numero.strip()}')
        cuadrado = [x**2 for x in numeros if x % 2 == 0]
        print(cuadrado)

except FileNotFoundError:
    print('Archivo No encontrado')
