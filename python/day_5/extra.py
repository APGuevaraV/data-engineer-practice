# Texto de entrada:
texto = "Hola mundo hola Python mundo código Python Hola"

# Requisitos:
# - Convertir el texto en palabras
# - Ignorar diferencias entre "Hola" y "hola"
# - Usar un set para eliminar duplicados
# - Mostrar una lista ordenada alfabéticamente

palabras = list(set(texto.lower().split(' ')))
palabras.sort()
print(palabras)


lista_a = [1, 2, 2, 3, 4, 5, 6]
lista_b = [4, 5, 6, 7, 8, 9]

# Requisitos:
# - Convertir ambas listas a sets
# - Obtener la diferencia: elementos únicos de lista_a que no están en lista_b
# - Mostrar el resultado como una lista ordenada ascendente


lista_a = set(lista_a)
lista_b = set(lista_b)
result = sorted(lista_a.difference(lista_b))
print(result)
