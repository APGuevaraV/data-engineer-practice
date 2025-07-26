estudiantes = [
    {"nombre": "Ana", "nota": 15},
    {"nombre": "Luis", "nota": 10},
    {"nombre": "María", "nota": 18},
    {"nombre": "Carlos", "nota": 8},
    {"nombre": "Sofía", "nota": 20}
]
aproved = [estudiante['nombre'] for estudiante in estudiantes
           if estudiante['nota'] >= 13]

with open('aprobados.text', 'w', encoding='utf8') as aprobados:
    for nombre in aproved:
        aprobados.write(nombre+"\n")
