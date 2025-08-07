import pandas as pd

ventas = pd.DataFrame({
    'ID_Venta': [11, 12, 13, 14, 15, 16],
    'ID_Producto': [101, 102, 103, 104, 102, 101],
    'Cantidad': [2, 3, 1, 5, 1, 3]
})

productos = pd.DataFrame({
    'ID_Producto': [101, 102, 103, 104, 105, 106, 107],
    'Nombre_Producto': ['Televisor', 'Celular', 'Laptop', 'Tablet',
                        'Audifonos', 'Mouse', 'Teclado'],
    'Precio': [1800, 1500, 2500, 899, 500, 120, 150]
})

join_df = pd.merge(productos, ventas, how='inner', on='ID_Producto')
join_df['Total Venta'] = join_df['Cantidad'] * join_df['Precio']
total_ventas_por_producto = join_df.groupby(
    'Nombre_Producto').agg({
        'Cantidad': 'sum',
        'Total Venta': 'sum'
    })

total_ventas_por_producto.sort_values(by='Total Venta', ascending=False)

ordered = total_ventas_por_producto.sort_values(by='Cantidad', ascending=False)
print(ordered[:3])
