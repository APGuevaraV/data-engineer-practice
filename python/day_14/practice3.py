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


df_text = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'producto': ['Laptop Pro', 'Laptop Air', 'Mouse Inalámbrico',
                 'Teclado Mecánico', 'Monitor 24"', 'USB 32GB'],
    'precio': [4500, 3500, 120, 500, 900, 50]
})

filtered_text = df_text[df_text['producto'].str.contains('Laptop')]
print(filtered_text)
filterd_df = df_text[~df_text['producto'].str.contains(
    'USB|Mouse', case=False, na=False)]
print(filterd_df)


df_text['precio_categoria'] = df_text['precio'].apply(
    lambda x:
    'Alto' if x > 2000 else
    'Medio'if 500 <= x <= 2000
    else 'Bajo'
)
print(df_text)


df_inter = pd.DataFrame({
    'pais': ['Perú', 'Chile', 'Argentina', 'Brasil', 'Perú', 'Chile', 'Perú',
             'Brasil'],
    'producto': ['Café', 'Café', 'Azúcar', 'Café', 'Azúcar', 'Cacao', 'Cacao',
                 'Café'],
    'cantidad': [15, 20, 8, 25, 30, 5, 12, 10],
    'precio_usd': [4, 4.2, 3, 4.5, 3.5, 6, 6, 4.2]
})

df_inter['total_ventas'] = df_inter['cantidad']*df_inter['precio_usd']
agrupado = df_inter.groupby('pais')['total_ventas'].sum()
print(agrupado)

ventas_mayores = df_inter[df_inter['total_ventas'] > 100]
print(ventas_mayores)

pivote_t = pd.pivot_table(
    df_inter, values=['cantidad'], columns=['producto'],
    index=['pais'], aggfunc={'cantidad': 'sum'}, fill_value=0)
print(pivote_t)


df_gastos = pd.DataFrame({
    'mes': ['Enero', 'Enero', 'Febrero', 'Febrero', 'Marzo', 'Marzo', 'Marzo'],
    'categoria': ['Alimentos', 'Transporte', 'Ocio', 'Alquiler', 'Servicios',
                  'Ocio', 'Alimentos'],
    'monto': [250, 60, 120, 800, 200, 300, 150]
})

print('\nGastos por mes\n')
gastos_por_mes = df_gastos.groupby('mes')['monto'].sum()
print(gastos_por_mes)
print(gastos_por_mes.idxmax())
pivote_gasto = pd.pivot_table(df_gastos, index=['mes'], columns=['categoria'],
                              values='monto', aggfunc='sum', fill_value=0)
print(pivote_gasto)
