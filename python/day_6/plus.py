from functools import reduce


empleados = [
    {"id": 1, "nombre": "Carlos Perez", "sueldo": 3800},
    {"id": 2, "nombre": "Lucía Fernández", "sueldo": 4500},
    {"id": 3, "nombre": "José Martínez", "sueldo": 5000},
    {"id": 4, "nombre": "María López", "sueldo": 3200},
    {"id": 5, "nombre": "Ana Gómez", "sueldo": 4700},
    {"id": 6, "nombre": "Pedro Sánchez", "sueldo": 3900},
    {"id": 7, "nombre": "Sofía Torres", "sueldo": 5200}
]


result = reduce(lambda x, y: x + y['sueldo'], empleados, 0)

print(result)
