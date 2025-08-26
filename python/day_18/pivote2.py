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
