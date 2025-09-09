from collections import defaultdict
import pandas as pd
import re
import multiprocessing as mp
import time


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


# lectura y escritura de archivo csv
df = pd.DataFrame({
    "producto": ["Laptop", "Mouse", "Teclado", "Monitor"],
    "cantidad": [3, 10, 5, 2],
    "precio": [3000, 50, 150, 800]
})

df.to_csv('csv/ventas.csv', index=False, encoding='utf-8')
df2 = pd.read_csv('csv/ventas.csv')
df2['total'] = df2['cantidad'] * df2['precio']
df2.to_csv('csv/reporte.csv', index=False)
print(df2)


emails = [
    "ana@example.com",
    "luis@empresa.com.pe",
    "maria123@gmail.com",
    "invalido@@.com",
    "jorge@dominio"
]

patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
validos = [email for email in emails if re.match(patron, email)]
print(validos)


data = {
    "empresa": "TechSolutions",
    "empleados": [
        {"nombre": "Ana", "skills": ["Python", "SQL", "AWS"]},
        {"nombre": "Luis", "skills": ["Java", "Spark"]},
        {"nombre": "María", "skills": ["Python", "Airflow", "GCP"]}
    ]
}

rows = []
for em in data['empleados']:
    for skill in em['skills']:
        rows.append({'nombre': em['nombre'], 'skill': skill})
df3 = pd.DataFrame(rows)
print(df3)


def cuadrado(x):
    return x * x


numeros = list(range(1, 1000000))
inicio = time.time()
res_normal = [cuadrado(x) for x in numeros]
print('Tiempo normal:', time.time() - inicio)

inicio = time.time()
with mp.Pool(processes=4) as pool:
    res_multi = pool.map(cuadrado, numeros)

print('Tiempo Multiprocesing:', time.time() - inicio)
