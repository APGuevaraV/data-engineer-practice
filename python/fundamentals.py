diccionario = {
    'nombre': 'Ana Paula',
    'edad': 29,
    'notas': []
}

n = int(input('Cantidad de notas a ingresar:'))
for i, nota in enumerate(range(n)):
    nota = int(input(f"Nota {i+1}:"))
    diccionario['notas'].append(nota)

for key in diccionario.keys():
    print(f"{key} , {diccionario[key]}")

promedio = sum(diccionario['notas']) / n

print(promedio)
