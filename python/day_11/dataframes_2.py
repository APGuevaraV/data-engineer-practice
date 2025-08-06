import pandas as pd

ventas_data = {
    'ID_Venta': [1, 2, 3, 4, 5, 6],
    'ID_Producto': [101, 102, 103, 104, 101, 105],
    'Cantidad': [2, 1, 5, 3, 4, None],
    'Fecha': ['2025-08-01', '2025-08-02', '2025-08-02', '2025-08-03',
              '2025-08-03', '2025-08-04']
}

ventas = pd.DataFrame(ventas_data)
productos_data = {
    'ID_Producto': [101, 102, 103, 104],
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor'],
    'Precio': [1500, 50, 80, 300]
}

productos = pd.DataFrame(productos_data)

# join de 2 dataframes
dos_df = ventas.merge(productos, on='ID_Producto', how='left')
print(dos_df)

dos_df['Cantidad'].fillna(1, inplace=True)
print(dos_df)

dos_df['Total Venta'] = dos_df['Cantidad']*dos_df['Precio']

agrupado = dos_df.groupby('Producto').agg({
    'Total Venta': 'sum',
    'Cantidad': 'sum'
}).reset_index()


agrupado.rename(columns={'Cantidad': 'Total_Cantidad'}, inplace=True)

agrupado = agrupado.sort_values(by='Total Venta', ascending=False)
print(agrupado)
print(agrupado.shape)
