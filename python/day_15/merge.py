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
