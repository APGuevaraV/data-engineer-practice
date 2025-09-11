from collections import defaultdict, Counter

alumnos = {
    "Ana": 15,
    "Luis": 18,
    "María": 15,
    "Pedro": 19,
    "Lucía": 18
}
result = defaultdict(list)
for key, value in alumnos.items():
    result[value].append(key)
print(result)


# 3
texto = "hoy es un buen día porque hoy aprendí Python"
lista = list(set(texto.split()))
print(lista)


matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
transpuesta = []
for i in range(len(matriz[0])):
    new_fila = []
    for fila in matriz:
        new_fila.append(fila[i])
    transpuesta.append(new_fila)


print(transpuesta)
# print(matriz.T)

# transpuesta
T = [list(fila) for fila in zip(*matriz)]
print(T)

cadena = "python power"
contador = Counter(cadena.replace(" ", ''))
print(contador)
