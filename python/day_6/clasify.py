from functools import reduce

alumnos = [
    {"nombre": "Carlos", "notas": [15, 18, 14, 17]},
    {"nombre": "Lucía", "notas": [20, 19, 18, 20]},
    {"nombre": "José", "notas": [12, 13, 11, 10]},
    {"nombre": "María", "notas": [16, 17, 16, 18]},
    {"nombre": "Ana", "notas": [13, 12, 6, 11]}
]

promedios = [
    {
        'nombre': alumno['nombre'],
        'promedio': reduce(lambda nota_1, nota_2: nota_1 + nota_2,
                           alumno['notas'], 0) // len(alumno['notas'])
    }
    for alumno in alumnos
]


resultado = {
    'aprobados': [x['nombre'] for x in promedios if x['promedio'] >= 14],
    'desaprobados': [x['nombre'] for x in promedios if x['promedio'] <= 14]
}

print(resultado)
