import pandas as pd

df = pd.DataFrame({
    'categoria': ['Electrónica', 'Electrónica', 'Hogar', 'Hogar', 'Ropa',
                  'Ropa', 'Electrónica'],
    'producto': ['Laptop', 'Mouse', 'Silla', 'Mesa', 'Camisa', 'Pantalón',
                 'Monitor'],
    'cantidad': [5, 20, 10, 4, 15, 8, 6],
    'precio_unitario': [3500, 50, 300, 500, 80, 120, 900]
})

df['total_ventas'] = df['cantidad']*df['precio_unitario']
filtered = df[df['total_ventas'] > 5000]
print(filtered)

pivote = pd.pivot_table(df, values=['cantidad', 'precio_unitario'], index=[
                        'categoria'], aggfunc={'cantidad': 'count',
                                               'precio_unitario': 'sum'})
print(pivote)


df_pedidos = pd.DataFrame({
    'pedido_id': [101, 102, 103, 104, 105, 106, 107],
    'cliente': ['Juan', 'Maria', 'Pedro', 'Lucia', 'Ana', 'Juan', 'Pedro'],
    'producto': ['Laptop', 'Mouse', 'Laptop', 'Teclado', 'Monitor', 'Laptop',
                 'Mouse'],
    'cantidad': [1, 2, 1, 3, 1, 2, 4],
    'precio': [3500, 50, 3500, 120, 900, 3500, 50]
})

print('\n Pedidos: \n')
df_pedidos['gasto_total'] = df_pedidos['cantidad']*df_pedidos['precio']
por_cliente = df_pedidos.groupby('cliente')['gasto_total'].sum()
maximo = por_cliente.idxmax()
print(por_cliente)
print('\n Maximo: \n')
print(maximo)
