import pandas as pd


df_ventas = pd.DataFrame({
    "Empleado": ["Ana", "Luis", "Ana", "Marta", "Luis", "Ana", "Pedro",
                 "Marta"],
    "Producto": ["Laptop", "Mouse", "Teclado", "Laptop", "Teclado", "Mouse",
                 "Laptop", "Teclado"],
    "Cantidad": [2, 5, 3, 1, 2, 4, 3, 2],
    "PrecioUnitario": [3000, 100, 200, 3000, 200, 100, 3000, 200],
    "Año": [2024, 2024, 2025, 2025, 2025, 2024, 2025, 2024]
})

df_ventas_resumen = df_ventas[df_ventas['Año'] == 2025].copy()
df_ventas_resumen.sort_values(
    by=['Empleado', 'Cantidad'], ascending=[True, False], inplace=True)
df_ventas_resumen.reset_index(inplace=True, drop=True)
# print(df_ventas_resumen)


df_objetivos = pd.DataFrame({
    "Empleado": ["Ana", "Luis", "Marta", "Pedro"],
    "ObjetivoAnual": [10000, 8000, 12000, 9000]
})

df_join = pd.merge(
    df_ventas,
    df_objetivos,
    how='left',
    on='Empleado'
)
df_join['TotalVendido'] = df_join['Cantidad']*df_join['PrecioUnitario']
# print(df_join)


df_clientes = pd.DataFrame({
    "ClienteID": [1, 2, 3, 4, 5],
    "Nombre": ["Carlos", "Lucía", "Andrés", "María", "Elena"],
    "Ciudad": ["Lima", "Trujillo", "Lima", "Arequipa", "Trujillo"]
})

df_clientes_nuevos = pd.DataFrame({
    "ClienteID": [3, 6, 7],
    "Nombre": ["Andrés", "Sofía", "Diego"],
    "Ciudad": ["Lima", "Cusco", "Lima"]
})

df_concatenado = pd.concat(
    [df_clientes,
     df_clientes_nuevos],
    axis=0
)
df_concatenado.drop_duplicates(inplace=True)
df_concatenado.reset_index()
print(df_concatenado)


df_facturas = pd.DataFrame({
    "FacturaID": [101, 102, 103, 104, 105, 106],
    "ClienteID": [1, 2, 3, 1, 5, 6],
    "Monto": [500, 1200, 800, 300, 1500, 700],
    "Fecha": pd.to_datetime(["2025-01-05", "2025-01-10", "2025-01-15",
                             "2025-02-01", "2025-02-05", "2025-02-10"])
})

join_df_facturas = pd.merge(
    df_clientes,
    df_facturas,
    how='left',
    on='ClienteID'
)
print(join_df_facturas)
