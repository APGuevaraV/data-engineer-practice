import pandas as pd

df = pd.read_csv('csv/productos.csv')

filtrado = df[(df['categoria'] == 'Tecnología') & (df['precio'] > 1500)]
print('\n Filtrados mayors a 1500 en Tecnología \n')
print(filtrado.reset_index())
print(filtrado.info())
print(filtrado.describe())
filtrado_ordered = filtrado.sort_values(by='precio', ascending=False)

# manejo de nan
filtered_nan = df.sort_values(by='precio', na_position='first')
print(filtered_nan.reset_index())
filtered_nan['precio'] = filtered_nan['precio'].fillna(
    filtered_nan['precio'].mean(), inplace=True)
print(filtered_nan)


# renombrar dinamicamente
df.columns = [
    "Fecha_" + col.replace("Fecha", "").strip().lower()
    if "Fecha" in col else col
    for col in df.columns
]
print("\nColumnas renombradas:\n", df.columns)
