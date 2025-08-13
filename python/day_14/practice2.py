import pandas as pd

df = pd.DataFrame({
    'pais': ['Perú', 'Chile', 'Argentina', 'Perú', 'Brasil', 'Chile', 'Perú'],
    'producto': ['Café', 'Café', 'Azúcar', 'Azúcar', 'Café', 'Azúcar',
                 'Cacao'],
    'cantidad': [15, 20, 8, 30, 25, 5, 12],
    'precio_usd': [4, 4.2, 3, 3.5, 4.5, 3.2, 6]
})

filtered = df[(df['pais'].isin(['Perú', 'Chile']))
              & (df['producto'] == 'Café')]
print(filtered)
filtered_country = df[(df['pais'] != 'Perú') & (df['precio_usd'] > 4)]
print(filtered_country)
df['total_ud'] = df['precio_usd']*df['cantidad']

df = df[df['total_ud'] > 60]
print(df.reset_index())


df_date = pd.DataFrame({
    'id': [101, 102, 103, 104, 105, 106],
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora', 'USB'],
    'stock': [5, 120, 30, 8, 10, 200],
    'precio_unitario': [3500, 50, 120, 900, 600, 25],
    'fecha_ingreso': pd.to_datetime([
        '2025-08-01', '2025-07-20', '2025-06-15', '2025-08-10', '2025-05-30',
        '2025-08-13'
    ])
})

stock_date = df_date[(df_date['stock'] < 20) & (
    df_date['fecha_ingreso'] > '2025-07-01')]
print(stock_date)

precios = df_date[(df_date['precio_unitario'] > 100) &
                  (df_date['precio_unitario'] < 1000)]
print(precios)

df_date['valor_total'] = df_date['precio_unitario'] * df_date['stock']
df_date = df_date[(df_date['valor_total'] > 5000) | (df_date['stock'] > 10)]
print(df_date)


df_pedidos = pd.DataFrame({
    'pedido_id': [1, 2, 3, 4, 5, 6, 7],
    'cliente': ['Juan', 'María', 'Pedro', 'Lucía', 'Carlos', 'Ana', 'Diego'],
    'cantidad': [3, 1, 5, 2, 4, 1, 7],
    'precio_unitario': [15, 50, 10, 30, 12, 200, 8],
    'estado': ['Entregado', 'Pendiente', 'Entregado', 'Cancelado', 'Pendiente',
               'Entregado', 'Entregado']
})

df_pedidos_f = df_pedidos[(df_pedidos['estado'] == 'Entregado')
                          & (df_pedidos['cantidad'] > 2)]
print('\n Pedidos \n')
print(df_pedidos_f)
pedidos_filtrados = df_pedidos[(df_pedidos['estado'].isin(
    ['Pendiente', 'Cancelado'])) & (df_pedidos['precio_unitario'] > 20)]
print(pedidos_filtrados)
df_pedidos['monto_total'] = df_pedidos['precio_unitario'] * \
    df_pedidos['cantidad']
df_pedidos = df_pedidos[df_pedidos['estado'] != 'Cancelado']
print(df_pedidos)
