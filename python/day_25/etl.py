import pandas as pd
import os


PATH_INPUTS = 'server_inputs'
PATH_OUTPUTS = 'server_outputs'
PATH_VENTAS = os.path.join(PATH_INPUTS, 'ventas_retailmax_raw.csv')
PATH_CLIENTES = os.path.join(PATH_INPUTS, 'clientes_retailmax_raw.csv')
PATH_PRODUCTOS = os.path.join(PATH_INPUTS, 'productos_retailmax_raw.csv')

PATH_RESUMEN = os.path.join(PATH_OUTPUTS, 'df_resumen.csv')

# Extract
df_ventas = pd.read_csv(PATH_VENTAS)
df_clientes = pd.read_csv(PATH_CLIENTES)
df_productos = pd.read_csv(PATH_PRODUCTOS)

# Transform
df_ventas["id_cliente"] = df_ventas["id_cliente"].astype(int)
df_ventas["id_producto"] = df_ventas["id_producto"].astype(int)
df_clientes["id_cliente"] = df_clientes["id_cliente"].astype(int)
df_productos["id_producto"] = df_productos["id_producto"].astype(int)

df_merge = df_ventas.merge(df_clientes, on="id_cliente", how="left")
df_merge = df_merge.merge(df_productos, on="id_producto", how="left")
df_merge["monto_venta"] = df_merge["cantidad"] * df_merge["precio_unitario"]

df_resumen = df_merge.groupby(["tipo_cliente", "categoria"])[
    "monto_venta"].sum().reset_index()
print(df_resumen)

# Load
df_resumen.to_csv(PATH_RESUMEN, index=False)
