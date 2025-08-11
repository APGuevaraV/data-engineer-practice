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

# setear indices
df_indexed = df.set_index('ID_PRODUCTO')
print("\n DataFrame con 'id_producto' como índice:\n", df_indexed.head())

df_reset = df_indexed.reset_index()
print("\n DataFrame con índice reseteado:\n", df_reset.head())

# crear copia del df
indice_personalizado = df.copy()
indice_personalizado.index = [f"row_{x}" for x in range(1, len(df)+1)]
print(indice_personalizado.head())

# practica
df = df.sort_values(by=['FECHA_INGRESO'], ascending=False)
print(df)

# filtrado
filtered_df = df[df['PRECIO_UNITARIO'] > df['PRECIO_UNITARIO'].quantile(0.75)]
print(filtered_df)
filtered_df.columns = ["".join(word.capitalize() for word in col.replace(
    "_", " ").split()) for col in filtered_df.columns]
print(filtered_df)

reindex = filtered_df.set_index('FechaIngreso')
print(reindex)
print(reindex.head(2))
print(reindex.tail(2))
