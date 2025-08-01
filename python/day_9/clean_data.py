import pandas as pd


productos = [
    {'producto': 'Laptop', 'categoria': 'Electrónica'},
    {'producto': 'Smartphone', 'categoria': 'electrónica'},
    {'producto': 'Polo', 'categoria': 'Ropa'},
    {'producto': 'Jeans', 'categoria': 'ROpa'}
]

df = pd.DataFrame(productos)
df['categoria'] = df['categoria'].str.capitalize()
prod_por_cat = df.groupby('categoria')['producto'].count().reset_index()
print(prod_por_cat)
