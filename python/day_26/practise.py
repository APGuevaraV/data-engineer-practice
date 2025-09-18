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
    how='inner',
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
df_concatenado.reset_index(drop=True, inplace=True)
# print(df_concatenado)


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
)[["ClienteID", "Nombre", "Ciudad", "Monto"]]
# print(join_df_facturas)


df_productos = pd.DataFrame({
    "ProductoID": [1, 2, 3, 4],
    "NombreProducto": ["Laptop", "Mouse", "Teclado", "Monitor"],
    "PrecioUnitario": [3000, 100, 200, 800]
})

df_productos.to_csv('productos.csv', index=False)
df_productos.to_json('productos.json', orient='records')

df_reader = pd.read_csv('productos.csv', encoding='utf-8')
# print(df_reader)


df_ventas_2 = pd.DataFrame({
    "Empleado": ["Ana", "Luis", "Ana", "Marta", "Luis", "Ana", "Pedro",
                 "Marta", "Luis", "Pedro"],
    "Producto": ["Laptop", "Mouse", "Teclado", "Laptop", "Teclado", "Mouse",
                 "Laptop", "Teclado", "Monitor", "Laptop"],
    "Cantidad": [2, 5, 3, 1, 2, 4, 3, 2, 1, 2],
    "PrecioUnitario": [3000, 100, 200, 3000, 200, 100, 3000, 200, 800, 3000],
    "Año": [2024, 2024, 2025, 2025, 2025, 2024, 2025, 2024, 2025, 2025]
})

df_ventas_2['Total vendido'] = df_ventas_2['Cantidad'] * \
    df_ventas_2['PrecioUnitario']
gb = df_ventas_2.groupby(['Empleado', 'Año'])[
    'Total vendido'].agg(['sum', 'mean', 'count'])
print(gb)

gb_prod = df_ventas_2.loc[df_ventas_2.groupby('Empleado')['Cantidad'].idxmax()]
print(gb_prod)


# Primero creamos una columna con el total vendido
df_ventas["Total"] = df_ventas["Cantidad"] * df_ventas["PrecioUnitario"]

# Calculamos el porcentaje por año usando transform
df_ventas["PorcentajeAño"] = (
    df_ventas["Total"] / df_ventas.groupby("Año")["Total"].transform("sum")
) * 100

print(df_ventas)

df_objetivos = pd.DataFrame({
    "Empleado": ["Ana", "Luis", "Marta", "Pedro"],
    "Objetivo2024": [8000, 5000, 9000, 7000],
    "Objetivo2025": [10000, 8000, 12000, 9000]
})

# Primero creamos el total vendido por empleado y año
df_totales = (
    df_ventas.assign(Total=lambda x: x["Cantidad"] * x["PrecioUnitario"])
    .groupby(["Empleado", "Año"], as_index=False)["Total"]
    .sum()
)

# Hacemos el join con los objetivos
df_join = pd.merge(df_totales, df_objetivos, on="Empleado", how="left")

# Comparamos según el año
df_join["Cumplió"] = df_join.apply(
    lambda row: "Sí" if (
        (row["Año"] == 2024 and row["Total"] >= row["Objetivo2024"]) or
        (row["Año"] == 2025 and row["Total"] >= row["Objetivo2025"])
    ) else "No",
    axis=1
)

print(df_join)


df_facturas['CategoriaVenta'] = df_facturas['Monto'].apply(
    lambda x: 'Bajo' if x < 50 else
    'Medio' if 500 <= x <= 2000
    else 'Alto'
)
print(df_facturas)
