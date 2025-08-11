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


# indices
ordered_fecha = df.set_index('Fecha_ingreso')
print(ordered_fecha.head())
ordered_fecha.sort_values(by='Fecha_ingreso', ascending=True)

df['Fecha_ingreso'] = pd.to_datetime(df['Fecha_ingreso'])

# 1. Usar 'Fecha_ingreso' como índice y ordenar
ordered_fecha = df.set_index('Fecha_ingreso').sort_index()
print("\nOrdenado por fecha:\n", ordered_fecha.head())

# 2. Slicing de fechas
slicing = ordered_fecha['2024-06-01':'2024-09-01']
print("\nFiltrado entre junio y septiembre:\n", slicing)

# 3. Resetear índice y agregar mes
slicing = slicing.reset_index()
slicing['mes_ingreso'] = slicing['Fecha_ingreso'].dt.month_name()
print("\nCon columna mes_ingreso:\n", slicing)


# manipular indices
categoria_muebles = df[(df['categoria'] == 'Muebles') & (df['stock'] > 10)]
print(categoria_muebles.head().reset_index())
stock_ordered = categoria_muebles.sort_values(
    by=['stock', 'precio'], ascending=[False, True])
stock_ordered.columns = [col.upper() for col in stock_ordered.columns]
print(stock_ordered.head())
