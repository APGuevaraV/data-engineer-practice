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
