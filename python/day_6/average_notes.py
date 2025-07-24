
alumnos = {
    "Carlos Perez": [15, 18, 14, 17],
    "Lucía Fernández": [20, 19, 18, 20],
    "José Martínez": [12, 14, 13, 15],
    "María López": [16, 17, 16, 18],
    "Ana Gómez": [19, 18, 17, 20],
    "Pedro Sánchez": [14, 16, 15, 17]
}

average_by_student = {
    nombre: sum(notas)/len(notas)
    for nombre, notas in alumnos.items()
}

print(average_by_student)
