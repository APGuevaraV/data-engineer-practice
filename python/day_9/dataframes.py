import pandas as pd

ventas = {
    'tienda': ['Tienda A', 'Tienda A', 'Tienda B', 'Tienda A', 'Tienda B'],
    'categoria': ['Electrónica', 'Electrónica', 'Electrónica', 'Ropa', 'Ropa'],
    'producto': ['Laptop', 'Smarthphone', 'Laptop', 'Polo', 'Polo'],
    'unidades_vendidas': [5, 10, 3, 20, 15]
}

df = pd.DataFrame(ventas)
por_tienda_por_categoria = df.groupby(['tienda', 'categoria'])[
    'unidades_vendidas'].sum().reset_index()

print(por_tienda_por_categoria)
