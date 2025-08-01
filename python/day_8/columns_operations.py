import pandas as pd

productos = {
    'producto': ['Lapiz', 'Cuaderno', 'Mochila'],
    'precio': [1.50, 5.00, 50.00],
    'stock': [100, 200, 50]
}
df = pd.DataFrame(productos)
df['valor total'] = df['precio'] * df['stock']

df['precio'] = df['precio'] * (1+10/100)
print(df)
filteres_price = df[df['valor total'] > 500]
print(filteres_price)
