import pandas as pd

# ==========================
# EJERCICIO 1:
# Ventas con información de clientes y productos
# ==========================
df_ventas = pd.DataFrame({
    "id_venta": [1, 2, 3, 4, 5],
    "id_cliente": [101, 102, 101, 103, 104],
    "id_producto": [201, 202, 201, 203, 204],
    "cantidad": [2, 1, 3, 5, 2]
})

df_clientes = pd.DataFrame({
    "id_cliente": [101, 102, 103],
    "nombre_cliente": ["Ana", "Luis", "Carla"],
    "ciudad": ["Lima", "Cusco", "Arequipa"]
})

df_productos = pd.DataFrame({
    "id_producto": [201, 202, 203],
    "producto": ["Laptop", "Mouse", "Monitor"],
    "precio_unitario": [3500, 50, 800]
})
# Une los tres DataFrames para obtener id_venta, nombre_cliente,
# ciudad, producto,
# cantidad y precio_unitario. Si algún cliente o producto no existe,
# debe aparecer como NaN.

ventas = pd.merge(df_ventas, df_clientes,
                  how='left',
                  on='id_cliente')
ventas = pd.merge(ventas, df_productos,
                  how='left',
                  on='id_producto')[['id_venta', 'nombre_cliente', 'ciudad',
                                    'producto',
                                     'cantidad', 'precio_unitario']]
print(ventas)


# ==========================
# EJERCICIO 2:
# Reporte de inventario y pedidos pendientes
# ==========================
df_inventario = pd.DataFrame({
    "id_producto": [1, 2, 3, 4],
    "producto": ["Silla", "Mesa", "Lámpara", "Sofá"],
    "stock": [10, 0, 5, 2]
})

df_pedidos_pendientes = pd.DataFrame({
    "id_pedido": [1001, 1002, 1003, 1004],
    "id_producto": [1, 2, 2, 4],
    "cantidad_pedida": [2, 1, 3, 2]
})

reporte = pd.merge(
    df_inventario[['id_producto', 'stock']],
    df_pedidos_pendientes[['id_producto', 'cantidad_pedida']],
    how='inner',
    on='id_producto'
)

reporte['stock_suficiente'] = (
    reporte['cantidad_pedida'] <= reporte['stock']).astype(bool)
print(reporte)


# ==========================
# EJERCICIO 3:
# Historial de precios
# ==========================
df_precios_2023 = pd.DataFrame({
    "id_producto": [1, 2, 3],
    "precio_2023": [100, 200, 300]
})

df_precios_2024 = pd.DataFrame({
    "id_producto": [1, 2, 4],
    "precio_2024": [110, 210, 400]
})

df_productos = pd.DataFrame({
    "id_producto": [1, 2, 3, 4],
    "producto": ["A", "B", "C", "D"]
})
# Primero concatena df_precios_2023 y df_precios_2024 verticalmente para un
# historial unificado.
# Luego haz un merge con df_productos para agregar el nombre del producto.

df_precios = pd.concat([df_precios_2023, df_precios_2024],
                       axis=0, ignore_index=True)
reporte_completo = df_precios.merge(
    df_productos, on='id_producto', how='inner'
)
print(reporte_completo)
