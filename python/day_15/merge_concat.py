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


# ==========================
# EJERCICIO 2
# ==========================
df_ventas_2023 = pd.DataFrame({
    "mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "ventas_2023": [1000, 1500, 1100, 1700]
})

df_ventas_2024 = pd.DataFrame({
    "mes": ["Febrero", "Marzo", "Abril", "Mayo"],
    "ventas_2024": [1600, 1200, 1800, 1900]
})

ambos_anios = pd.merge(
    df_ventas_2023,
    df_ventas_2024,
    how='outer',
    on='mes'
)

print(ambos_anios)


# ==========================
# EJERCICIO 3
# ==========================
df_sucursal_a = pd.DataFrame({
    "producto": ["Laptop", "Mouse", "Teclado"],
    "stock": [10, 50, 30]
})

df_sucursal_b = pd.DataFrame({
    "producto": ["Monitor", "Mouse", "Parlante"],
    "stock": [20, 40, 15]
})

a_b = pd.concat([df_sucursal_a, df_sucursal_b], axis=0, ignore_index=True)
print(a_b)

# ==========================
# EJERCICIO 4
# ==========================
df_clientes_4 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "nombre": ["Pedro", "María", "José", "Lucía"],
    "pais": ["Perú", "Chile", "Perú", "Brasil"]
})

df_paises = pd.DataFrame({
    "pais": ["Perú", "Chile", "Argentina"],
    "continente": ["América", "América", "América"]
})

clientes_paises = df_clientes_4.merge(df_paises,
                                      how='inner',
                                      on='pais')
print(clientes_paises)


# ==========================
# EJERCICIO 5
# ==========================
df_parte1 = pd.DataFrame({
    "id": [1, 2],
    "dato": ["A", "B"]
})

df_parte2 = pd.DataFrame({
    "id": [3, 4],
    "dato": ["C", "D"]
})

df_parte3 = pd.DataFrame({
    "id": [5, 6],
    "dato": ["E", "F"]
})

result = pd.concat([df_parte1, df_parte2, df_parte3],
                   axis=0, ignore_index=True)
result_horiz = pd.concat([df_parte1, df_parte2, df_parte3],
                         axis=1)
print(result)
print(result_horiz)
