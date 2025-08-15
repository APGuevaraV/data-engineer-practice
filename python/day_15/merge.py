import pandas as pd

# ==========================
# EJERCICIO 1:
# Combinar inventario con precios
# ==========================
df_inventario = pd.DataFrame({
    "id_producto": [101, 102, 103, 104],
    "producto": ["Laptop", "Mouse", "Teclado", "Monitor"],
    "stock": [15, 100, 50, 20]
})

df_precios = pd.DataFrame({
    "id_producto": [101, 102, 104, 105],
    "precio_unitario": [3500, 50, 800, 200]
})
# Une ambos para obtener un DataFrame con producto, stock
# y precio_unitario (left join)
inventario_precios = df_inventario.merge(df_precios,
                                         how='left',
                                         on='id_producto')[['producto',
                                                            'stock',
                                                            'precio_unitario']]
print(inventario_precios)


# ==========================
# EJERCICIO 2:
# Ventas por empleado en dos años
# ==========================
df_ventas_2023 = pd.DataFrame({
    "id_empleado": [1, 2, 3],
    "ventas_2023": [25000, 30000, 18000]
})

df_ventas_2024 = pd.DataFrame({
    "id_empleado": [2, 3, 4],
    "ventas_2024": [32000, 21000, 15000]
})

df_empleados = pd.DataFrame({
    "id_empleado": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "Carla", "Jorge"]
})

ventas = pd.merge(df_ventas_2023, df_ventas_2024,
                  on='id_empleado',
                  how='outer')

ventas = pd.merge(ventas, df_empleados,
                  on='id_empleado',
                  how='outer')[['id_empleado', 'nombre']]
print(ventas)
