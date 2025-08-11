import pandas as pd

df = pd.read_csv('csv/inventory.csv')
# print(df)
# primera 3 columnas
print(df.head(3))
print(df.tail(5))
print('shape del df')
print(df.shape)
# tipos de datos
print(df.info())
print(df.describe(include='object'))


# ordenarmiento
sorted_df = df.sort_values(by='precio', ascending=False)
print(sorted_df)
sorted_two_fields = df.sort_values(by=['categoria', 'stock'])
print(sorted_two_fields)
upper_average = df[df['stock'] > df['stock'].mean()]
print('Mayor que el promedio en stock:', df['stock'].mean())
print(upper_average)

# columnas a snake

df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
print(df.columns)
# renombrar columns
df.rename(columns={
    'stock': 'inventario',
    'precio': 'precio_unitario'
}, inplace=True)
print(df)

# columas a mayusculas
df.columns = [col.upper() for col in df.columns]
print(df.columns)
