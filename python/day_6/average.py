from functools import reduce
"""
alumnoss = {
    "Carlos": [15, 18, 14, 17],
    "Lucía": [20, 19, 18, 20],
    "José": [12, 14, 13, 15],
    "María": [16, 17, 16, 18],
    "Ana": [19, 18, 17, 20]
}
"""


def promedio(alumnos: dict):
    for alumno in alumnos.keys():
        promedio = reduce(lambda x, y: x+y,
                          alumnos[alumno]) / len(alumnos[alumno])
        print(f"Alumno:{alumno} - promedio :{promedio}")


def crear_diccionario(contador: int, alumnos: dict):

    nombre = input(f'Alumno {contador +1}: ')
    while nombre in alumnos:
        print('Alumno ya registrado')
        nombre = input(f'Alumno {contador +1}: ')

    notas = [int(input('Notas: ')) for x in range(0, 4)]
    alumnos[nombre.lower()] = notas


alumnos = {}
for i, x in enumerate(range(0, 5)):
    crear_diccionario(i, alumnos)
promedio(alumnos)
