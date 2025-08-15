import pandas as pd

# ==========================
# EJERCICIO 1
# ==========================
df_clientes = pd.DataFrame({
    "id_cliente": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "Carla", "Jorge"],
    "ciudad": ["Lima", "Cusco", "Lima", "Arequipa"]
})

df_pedidos = pd.DataFrame({
    "id_pedido": [101, 102, 103, 104, 105],
    "id_cliente": [1, 3, 2, 1, 4],
    "monto": [150, 200, 350, 100, 400]
})

clientes_pedidos = pd.merge(df_clientes, df_pedidos,
                            how='inner',
                            on='id_cliente')
print(clientes_pedidos[['nombre', 'ciudad', 'monto']])
