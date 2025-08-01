import pandas as pd

clientes = {
    'clienteID': [1, 2, 3],
    'Nombre': ['Ana', 'Luis', 'Carla']
}

ordenes = {
    'OrdeID': [101, 102, 102, 104],
    'clienteID': [1, 3, 2, 1],
    'Monto': [500, 700, 300, 200],
}

df_clientes = pd.DataFrame(clientes)
df_ordenes = pd.DataFrame(ordenes)
df_result = df_ordenes.merge(
    df_clientes, left_on='clienteID', right_on='clienteID')

monto_por_cliente = df_result.groupby('Nombre')['Monto'].sum().reset_index()
print(monto_por_cliente)

monto_por_cliente = monto_por_cliente.sort_values(by='Monto', ascending=False)
