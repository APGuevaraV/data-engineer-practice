empleados = [
    {"nombre": "Carlos Perez", "sueldo": 3800},
    {"nombre": "Lucía Fernández", "sueldo": 4500},
    {"nombre": "José Martínez", "sueldo": 5000},
    {"nombre": "María López", "sueldo": 3200},
    {"nombre": "Ana Gómez", "sueldo": 4700},
    {"nombre": "Pedro Sánchez", "sueldo": 3900},
    {"nombre": "Sofía Torres", "sueldo": 5200}
]

increased_salary = list(map(lambda x: int(x['sueldo']*1.10), empleados))

for x in increased_salary:
    print(f"salario incrementado :{x}")
