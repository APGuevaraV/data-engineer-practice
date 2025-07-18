import random


def clasify(notes: list):
    for x in notes:
        if x < 10:
            print(f"{x} - Desaprobado")
        elif x < 18:
            print(f"{x} - Aprobado")
        else:
            print(f"{x} - Excelente")


print("Final Notes:")
notes = [random.randint(0, 20) for x in range(10)]
clasify(notes=notes)


def serie_fibonacci(n):
    a, b = 0, 1
    contador = 0
    serie = []

    while contador < n:
        serie.append(a)
        a, b = b, a + b
        contador += 1

    return serie


print(f"Serie :{serie_fibonacci(25)}")


def high_value(diccionario: dict):
    mayor = max(diccionario, key=diccionario.get)
    return f"{mayor} - {diccionario[mayor]}"


diccionario = {
    'nota1': 17,
    'nota2': 11,
    'nota3': 4,
    'nota4': 9,
    'nota5': 13,
    'nota6': 10,
    'nota7': 15,
    'nota8': 19,
}

print(high_value(diccionario))
