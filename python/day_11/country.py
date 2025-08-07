import pandas as pd

transacciones = pd.DataFrame({
    'ID_Transacción': [101, 102, 103, 104, 105, 106],
    'País': ['Perú', 'Colombia', 'Brasil', 'Uruguay', 'Canadá', 'Perú'],
    'Monto': [1025, 2451, 3648, 1248, 2567, 7855],
    'Método_Pago': ['Tarjeta', 'Efectivo', 'Transferencia', 'Tarjeta',
                    'Efectivo', 'Transferencia']
})

group_table = transacciones.groupby(['País', 'Método_Pago']).agg({
    'Monto': 'sum'
})
print(group_table)
pivot = group_table.pivot_table(
    values='Monto',
    columns='Método_Pago',
    index='País',
    fill_value=0
)
print(pivot)
print(pivot.shape)
pais_facturo_mas = pivot['Tarjeta'].idxmax()
monto_facturo_mas = pivot['Tarjeta'].max()
