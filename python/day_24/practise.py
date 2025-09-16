import pandas as pd

# Dataset 1: Ventas
df_ventas = pd.DataFrame({
    "Empleado": ["Ana", "Luis", "Ana", "Pedro", "Luis", "Pedro", "Ana"],
    "Año": [2023, 2023, 2024, 2023, 2024, 2024, 2025],
    "Ventas": [1500, 2300, 1800, 2200, 2500, 2100, 3000]
})

anio_2023 = df_ventas[(df_ventas['Año'] ==
                      2023) & (df_ventas['Empleado'] == 'Ana')].sort_values(by='Ventas', ascending=False)
# print(anio_2023)

# Dataset 2: Productos
df_productos = pd.DataFrame({
    "ProductoID": [1, 2, 3, 4],
    "Nombre": ["Laptop", "Mouse", "Teclado", "Monitor"],
    "Precio": [3500, 50, 100, 800]
})

# Dataset 3: Detalle ventas
df_detalle = pd.DataFrame({
    "VentaID": [101, 102, 103, 104, 105, 106],
    "ProductoID": [1, 2, 2, 3, 4, 1],
    "Cantidad": [1, 3, 2, 5, 2, 1]
})

nuevo_df = pd.merge(df_productos, df_detalle, how='inner', on='ProductoID')
nuevo_df['total'] = nuevo_df['Cantidad']*nuevo_df['Precio']
gb_producto = nuevo_df.groupby('ProductoID')['total'].sum()
# print(gb_producto)

# Dataset 4: Clientes
df_clientes = pd.DataFrame({
    "ClienteID": [10, 11, 12, 13],
    "Nombre": ["Carlos", "María", "José", "Lucía"],
    "Ciudad": ["Lima", "Cusco", "Lima", "Arequipa"]
})

# Dataset 5: Órdenes
df_ordenes = pd.DataFrame({
    "OrdenID": [101, 102, 103, 104, 105, 106],
    "ClienteID": [10, 11, 12, 13, 10, 12],
    "Fecha": pd.to_datetime(["2024-01-15", "2024-01-20", "2024-02-10",
                             "2024-02-18", "2024-03-05", "2024-03-22"])
})

join_cliente_orden = pd.merge(
    df_clientes,
    df_ordenes,
    how='inner',
    on='ClienteID'
)
# print(join_cliente_orden)

df_ventas_before = df_ventas[df_ventas['Año'] < 2024]
df_ventas_from = df_ventas[df_ventas['Año'] >= 2024]

concatenacion = pd.concat([df_ventas_before, df_ventas_from], axis=0)
print(concatenacion)
