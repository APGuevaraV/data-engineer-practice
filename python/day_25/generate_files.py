import pandas as pd
import os

PATH_INPUTS = 'server_inputs'
PATH_OUTPUTS = 'server_outputs'
PATH_VENTAS = os.path.join(PATH_INPUTS, 'ventas_retailmax_raw.csv')
PATH_CLIENTES = os.path.join(PATH_INPUTS, 'clientes_retailmax_raw.csv')
PATH_PRODUCTOS = os.path.join(PATH_INPUTS, 'productos_retailmax_raw.csv')

if not os.path.exists(PATH_INPUTS):
    os.makedirs(PATH_INPUTS)

if not os.path.exists(PATH_OUTPUTS):
    os.makedirs(PATH_OUTPUTS)

# Dataset de ventas
ventas = {
    "id_venta": [1, 2, 3, 4, 5],
    "id_cliente": [101, 102, 103, 101, 104],
    "id_producto": [1001, 1002, 1003, 1001, 1002],
    "fecha_venta": ["2025-08-01", "2025-08-01", "2025-08-02", "2025-08-02",
                    "2025-08-03"],
    "cantidad": [2, 1, 3, 5, 2],
    "precio_unitario": [100, 200, 50, 100, 200]
}

df_ventas = pd.DataFrame(ventas)
df_ventas.to_csv(PATH_VENTAS, index=False)


# Dataset de clientes
clientes = {
    "id_cliente": [101, 102, 103, 104],
    "tipo_cliente": ["Retail", "Mayorista", "Retail", "VIP"]
}

df_clientes = pd.DataFrame(clientes)
df_clientes.to_csv(PATH_CLIENTES, index=False)

# Dataset de productos
productos = {
    "id_producto": [1001, 1002, 1003],
    "categoria": ["Electrónica", "Ropa", "Hogar"]
}

df_productos = pd.DataFrame(productos)
df_productos.to_csv(PATH_PRODUCTOS, index=False)
