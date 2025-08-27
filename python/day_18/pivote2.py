import pandas as pd

data = {
    "Vendedor": ["Ana", "Ana", "Luis", "Luis", "Carla", "Carla", "Pedro",
                 "Pedro"],
    "Producto": ["Laptop", "Mouse", "Laptop", "Monitor", "Mouse", "Teclado",
                 "Laptop", "Teclado"],
    "Región": ["Norte", "Sur", "Norte", "Norte", "Sur", "Norte", "Sur", "Sur"],
    "Ventas": [2000, 500, 2500, 1500, 400, 700, 2200, 800],
    "Unidades": [2, 5, 3, 2, 4, 7, 2, 6]
}

df6 = pd.DataFrame(data)
print(df6)

pivote_products = pd.pivot_table(
    df6,
    index='Producto',
    columns='Región',
    values=['Ventas', 'Unidades'],
    aggfunc={
        'Ventas': ['sum', 'mean'],
        'Unidades': 'sum'
    },
    fill_value=0
)
print(pivote_products)


data = {
    "Empleado": ["Ana", "Luis", "Carla", "Pedro", "Ana", "Luis", "Carla",
                 "Pedro", "Ana", "Luis"],
    "Departamento": ["TI", "TI", "Ventas", "Ventas", "TI", "Ventas", "TI",
                     "Ventas", "TI", "Ventas"],
    "Mes": ["Enero", "Enero", "Enero", "Enero", "Febrero", "Febrero",
            "Febrero", "Febrero", "Marzo", "Marzo"],
    "Horas": [160, 150, 170, 165, 155, 160, 145, 150, 170, 180],
    "Proyectos": [3, 2, 4, 3, 2, 5, 3, 4, 4, 6]
}

df7 = pd.DataFrame(data)
print(df7)
pivote_horas = pd.pivot_table(
    df7,
    index='Departamento',
    columns='Mes',
    values=['Horas', 'Proyectos'],
    aggfunc={
        'Horas': 'mean',
        'Proyectos': 'sum'
    },
    margins=True,
    fill_value=0
)
print(pivote_horas)


data = {
    "Cliente": ["Juan", "Ana", "Luis", "Pedro", "Juan", "Ana", "Luis",
                "Pedro", "Juan", "Ana"],
    "Categoría": ["Electrónica", "Electrónica", "Ropa", "Electrónica",
                  "Ropa", "Ropa", "Electrónica", "Ropa", "Electrónica", "Ropa"
                  ],
    "Producto": ["Laptop", "Mouse", "Camisa", "Laptop", "Pantalón",
                 "Zapatos", "Tablet", "Zapatos", "Celular", "Camisa"],
    "Cantidad": [1, 2, 3, 1, 2, 1, 2, 1, 1, 4],
    "PrecioUnit": [2000, 50, 40, 2200, 60, 100, 500, 120, 800, 45]
}

df8 = pd.DataFrame(data)
print(df8)
df8['Monto'] = df8['Cantidad'] * df8['PrecioUnit']
pivote_pedidos = pd.pivot_table(
    df8,
    index='Cliente',
    columns=['Categoría', 'Producto'],
    values='Monto',
    aggfunc='sum',
    fill_value=0
)
print(pivote_pedidos)


data = {
    "Estudiante": ["Ana", "Luis", "Carla", "Pedro", "Ana", "Luis", "Carla",
                   "Pedro", "Ana", "Luis"],
    "Curso": ["Math", "Math", "Science", "Science", "History", "History",
              "Math", "Science", "Math", "History"],
    "Semestre": ["2024-1", "2024-1", "2024-1", "2024-1", "2024-2", "2024-2",
                 "2024-2", "2024-2", "2024-3", "2024-3"],
    "Nota": [15, 18, 20, 12, 16, 19, 14, 17, 13, 20]
}

df9 = pd.DataFrame(data)
print(df9)

pivote_semestre = pd.pivot_table(
    df9,
    index='Curso',
    columns='Semestre',
    values='Nota',
    aggfunc=['mean', 'max', 'min'],
    fill_value=0
)

print(pivote_semestre)


data = {
    "Planta": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
    "Mes": ["Enero", "Febrero", "Marzo", "Enero", "Febrero",
            "Marzo", "Enero", "Febrero", "Marzo"],
    "Producto": ["X", "X", "X", "Y", "Y", "Y", "Z", "Z", "Z"],
    "Producción": [100, 120, 130, 200, 220, 210, 150, 140, 160],
    "Defectuosos": [5, 6, 4, 10, 8, 9, 7, 6, 5]
}

df10 = pd.DataFrame(data)
print(df10)

df10['porc_defectuosos'] = (df10['Defectuosos']/df10['Producción'])*100

pivote_produccion = pd.pivot_table(
    df10,
    index='Planta',
    columns='Mes',
    values=['Producción', 'Defectuosos'],
    aggfunc='sum'
)


print(pivote_produccion)


data = {
    "estudiante": ["Ana", "Ana", "Luis", "Luis", "Carla", "Carla", "Ana",
                   "Luis"],
    "curso": ["Matemáticas", "Historia", "Matemáticas", "Historia",
              "Matemáticas", "Historia", "Ciencias", "Ciencias"],
    "nota": [15, 18, 12, 16, 20, 19, 17, 14],
    "semestre": ["2024-I", "2024-I", "2024-I", "2024-I", "2024-II", "2024-II",
                 "2024-II", "2024-II"]
}
df = pd.DataFrame(data)
print(df)

pivote_calificaciones = pd.pivot_table(
    df,
    index='estudiante',
    columns='semestre',
    values='nota',
    aggfunc=['mean', 'max', 'min'],
    fill_value=0
)
pivote_curso = pd.pivot_table(
    df,
    index='curso',
    columns='semestre',
    values='nota',
    aggfunc=['max', 'min'],
    fill_value=0
)
print(pivote_curso)

print(pivote_calificaciones)

data12 = {
    "region": ["Norte", "Norte", "Norte", "Sur", "Sur", "Sur", "Este", "Este"],
    "producto": ["A", "B", "C", "A", "B", "C", "A", "B"],
    "ventas": [1200, 800, 600, 1500, 900, 700, 1100, 950],
    "mes": ["Enero", "Enero", "Enero", "Febrero", "Febrero", "Febrero",
            "Marzo", "Marzo"]
}
df12 = pd.DataFrame(data12)
print(df12)


ventas_totales = pd.pivot_table(
    df12,
    index='region',
    columns='mes',
    values='ventas',
    aggfunc='sum',
    fill_value=0
)


ventas_promedio = pd.pivot_table(
    df12,
    index='region',
    columns='producto',
    values='ventas',
    aggfunc='mean',
    fill_value=0
)


data = {
    "agente": ["Juan", "Juan", "María", "María", "Luis", "Luis", "Ana", "Ana"],
    "día": ["Lunes", "Martes", "Lunes", "Martes", "Lunes", "Martes", "Lunes",
            "Martes"],
    "llamadas": [30, 28, 25, 27, 35, 33, 20, 22],
    "tiempo_promedio": [4.5, 4.2, 5.0, 4.8, 3.8, 4.0, 6.0, 5.8]
}
df13 = pd.DataFrame(data)
print(df13)
pivote_tiempo = pd.pivot_table(
    df13,
    index='agente',
    values=['llamadas', 'tiempo_promedio'],
    aggfunc={
        'llamadas': 'sum',
        'tiempo_promedio': 'mean'
    },
    fill_value=0
)
print(pivote_tiempo)
