import pandas as pd

personas = [
    {'Nombre': 'Ana', 'Edad': 25, 'Ciudad': 'Lima'},
    {'Nombre': 'Carlos', 'Edad': 30, 'Ciudad': 'Arequipa'},
    {'Nombre': 'María', 'Edad': 22, 'Ciudad': 'Cusco'}
]

df = pd.DataFrame(personas)
print(df['Nombre'])
print(df.iloc[1])


data = {
    'Producto': ['Laptop', 'Celular', 'Tablet'],
    'Precio': [3500, 1500, 2200],
    'Stock': [10, 25, 15]
}

df_products = pd.DataFrame(data)
print(df_products[df_products['Stock'] > 15])
print(f"precio tablet {df_products['Precio'].iloc[2]}")

primeras_dos = df_products.iloc[:2]
print(primeras_dos)
last_row = df_products.iloc[-1]
print(last_row)
