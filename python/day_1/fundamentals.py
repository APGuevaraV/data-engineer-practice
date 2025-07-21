# Crear un diccionario que represente un estudiante con nombre, edad y notas.
# Agregar una nota y calcular el promedio.
diccionario = {
    'nombre': 'Ana Paula',
    'edad': 29,
    'notas': []
}

"""
n = int(input('Cantidad de notas a ingresar:'))
for i, nota in enumerate(range(n)):
    nota = int(input(f"Nota {i+1}:"))
    diccionario['notas'].append(nota)

for key in diccionario.keys():
    print(f"{key} , {diccionario[key]}")

promedio = sum(diccionario['notas']) / n

print(promedio)
"""

# Dado un texto, contar cuántas veces aparece cada letra (usa diccionario).

text = """There is no one who loves pain itself, who seeks after it and
        wants to have it, simply because it is pain"""

letras = list(set(text.lower()
                  .replace(' ', '')
                  .replace('\n', '')))

lists = []
for letra in letras:
    apariciones = text.count(letra)
    lists.append((letra, apariciones))

print(dict(lists))

lista_de_pares = [x for x in range(1, 101) if x % 2 == 0]
print(lista_de_pares)
