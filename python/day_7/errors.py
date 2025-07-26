pares = [(10, 2), (5, 0), (8, 4), (15, 3), (7, 0)]
result = []
for a, b in pares:
    try:
        division = a/b
    except ZeroDivisionError:
        print('No se puede dividir entre cero')
    else:
        result.append(division)
print(result)
