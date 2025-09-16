import pandas as pd
import numpy as np

# Dataset Ventas
df_ventas = pd.DataFrame({
    "VentaID": [1, 2, 3, 4, 5, 6, 7],
    "Empleado": ["Ana", "Luis", "Ana", "Pedro", "Luis", "Pedro", "Ana"],
    "Producto": ["Laptop", "Mouse", "Monitor", "Laptop", "Teclado", "Mouse",
                 "Teclado"],
    "Cantidad": [1, 2, 1, 1, 3, 4, 2],
    "PrecioUnitario": [3500, 50, 800, 3500, 100, 50, 100],
    "Fecha": pd.to_datetime([
        "2024-01-15", "2024-01-20", "2024-02-05",
        "2024-02-18", "2024-03-01", "2024-03-12", "2024-03-25"
    ])
})

df_ventas['total vendido'] = df_ventas['Cantidad'] * \
    df_ventas['PrecioUnitario']
gb_total = df_ventas.groupby(['Empleado', 'Producto'])['total vendido'].sum()
# print(gb_total)

# Dataset Objetivos de venta
df_objetivos = pd.DataFrame({
    "Empleado": ["Ana", "Luis", "Pedro"],
    "ObjetivoMensual": [5000, 4000, 3000]
})

join_ventas = pd.merge(
    df_ventas,
    df_objetivos,
    how='inner',
    on='Empleado'
)
ventas_2024 = join_ventas[join_ventas['Fecha'].dt.year == 2024]
ventas_2024['Cumplimiento'] = np.where(
    ventas_2024['total vendido'] < ventas_2024['ObjetivoMensual'],
    'No',
    'Sí'
)

print(ventas_2024)

# Dataset Clientes
df_clientes = pd.DataFrame({
    "ClienteID": [10, 11, 12, 13, 14],
    "NombreCliente": ["Carlos", "María", "José", "Lucía", "Elena"],
    "Ciudad": ["Lima", "Cusco", "Lima", "Arequipa", "Cusco"]
})
