import pandas as pd

data = {
    "Empleado": ["Ana", "Ana", "Luis", "Luis", "Carla", "Carla", "Pedro",
                 "Pedro"],
    "Departamento": ["Ventas", "Marketing", "Ventas", "Marketing", "Ventas",
                     "Marketing", "Ventas", "Marketing"],
    "Mes": ["Enero", "Enero", "Enero", "Febrero", "Febrero", "Enero",
            "Febrero", "Febrero"],
    "Ventas": [2000, 1800, 2200, 2100, 2500, 2300, 1900, 1700],
    "Horas": [160, 150, 170, 165, 155, 145, 160, 150]
}

df = pd.DataFrame(data)
print(df)


by_employyee = pd.pivot_table(
    df, index="Empleado", values="Ventas", aggfunc="sum")
print(by_employyee)

depto_employee = pd.pivot_table(
    df, index="Empleado", columns="Departamento", values="Ventas",
    aggfunc="sum")
print(depto_employee)


data = {
    "Producto": ["Laptop", "Laptop", "Mouse", "Mouse", "Teclado", "Teclado",
                 "Monitor", "Monitor"],
    "Región": ["Norte", "Sur", "Norte", "Sur", "Norte", "Sur", "Norte", "Sur"],
    "Vendedor": ["Ana", "Luis", "Ana", "Carla", "Pedro", "Ana", "Luis",
                 "Carla"],
    "Ventas": [1200, 1500, 200, 250, 400, 500, 800, 900]
}

df1 = pd.DataFrame(data)
print(df1)
pivote_ventas = pd.pivot_table(
    df1,
    index='Producto',
    columns='Región',
    values='Ventas',
    aggfunc='sum',
    fill_value=0
)

print(pivote_ventas)


data = {
    "Empleado": ["Ana", "Luis", "Carla", "Pedro", "Ana", "Luis", "Carla",
                 "Pedro"],
    "Proyecto": ["A", "A", "B", "B", "C", "C", "A", "C"],
    "Mes": ["Enero", "Enero", "Febrero", "Febrero", "Enero", "Febrero",
            "Enero", "Febrero"],
    "Horas": [40, 42, 38, 35, 50, 48, 30, 45]
}

df2 = pd.DataFrame(data)
print(df2)

by_employyee_project = pd.pivot_table(
    df2,
    index='Empleado',
    columns='Proyecto',
    values='Horas',
    aggfunc='mean',
    fill_value=0
)
print(by_employyee_project)


data = {
    "Cliente": ["Juan", "Ana", "Pedro", "Luis", "Ana", "Pedro", "Juan",
                "Luis"],
    "Producto": ["Zapatos", "Zapatos", "Camisa", "Zapatos", "Camisa",
                 "Zapatos", "Camisa", "Zapatos"],
    "Cantidad": [2, 1, 3, 2, 2, 1, 1, 4],
    "PrecioUnit": [100, 100, 50, 100, 50, 100, 50, 100]
}

df3 = pd.DataFrame(data)
df3['monto_total'] = df3['Cantidad']*df3['PrecioUnit']
print(df3)
compras = pd.pivot_table(
    df3,
    index='Cliente',
    columns='Producto',
    values='monto_total',
    aggfunc='sum',
    fill_value=0)
print(compras)


data = {
    "Estudiante": ["Ana", "Luis", "Carla", "Pedro", "Ana", "Luis", "Carla",
                   "Pedro"],
    "Curso": ["Math", "Math", "Science", "Science", "History", "History",
              "Math", "Science"],
    "Nota": [15, 18, 20, 12, 16, 19, 14, 17],
    "Semestre": ["2024-1", "2024-1", "2024-1", "2024-1", "2024-2", "2024-2",
                 "2024-2", "2024-2"]
}

df4 = pd.DataFrame(data)
print(df4)
notas = pd.pivot_table(
    df4,
    index='Curso',
    columns='Semestre',
    values='Nota',
    aggfunc='mean',
    fill_value=0
)
print(notas)


data = {
    "Cliente": ["Ana", "Luis", "Carla", "Pedro", "Ana", "Luis", "Carla",
                "Pedro", "Ana"],
    "Hotel": ["Marriott", "Hilton", "Marriott", "Hilton", "Hilton",
              "Marriott", "Hilton", "Hilton", "Marriott"],
    "Noches": [3, 2, 4, 1, 5, 3, 2, 6, 4],
    "CostoNoche": [120, 150, 120, 150, 150, 120, 150, 150, 120]
}

df5 = pd.DataFrame(data)
print(df5)
df5['Costo_total'] = df5['Noches']*df5['CostoNoche']
hotel_reservations = pd.pivot_table(
    df5,
    index='Cliente',
    columns='Hotel',
    values='Costo_total',
    aggfunc='sum',
    fill_value=0
)

print(hotel_reservations)
