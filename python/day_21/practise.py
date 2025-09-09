from collections import defaultdict

empleados = [
    {"id": 1, "nombre": "Ana", "departamento": "IT", "salario": 5500},
    {"id": 2, "nombre": "Luis", "departamento": "HR", "salario": 4200},
    {"id": 3, "nombre": "María", "departamento": "IT", "salario": 6100},
    {"id": 4, "nombre": "Jorge", "departamento": "Finance", "salario": 4800},
    {"id": 5, "nombre": "Lucía", "departamento": "Finance", "salario": 5300},
]

dept_salarios = defaultdict(list)

for empleado in empleados:
    dept_salarios[empleado['departamento']].append(empleado['salario'])

promedio = {
    dept: sum(salario)/len(salario)
    for dept, salario in dept_salarios.items()
}

print(promedio)
