import pandas as pd


ventas = {
    'ID': [1, 2, 3, 4, 5],
    'Producto': ['Laptop', 'Mouse', 'Laptop', 'Teclado', 'Mouse'],
    'Precio': [3500, 50, 3500, 80, 50]
}

df = pd.DataFrame(ventas)
df.drop_duplicates(subset=['Producto'], inplace=True)
print(df)
