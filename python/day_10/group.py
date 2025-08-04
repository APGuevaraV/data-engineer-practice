import pandas as pd


ventas = pd.DataFrame({
    'Producto': ['Laptop', 'Celular', 'Tablet', 'Laptop', 'Tablet'],
    'Precio': [3500, 1500, 2200, 3700, 2100],
    'Unidades': [3, 10, 5, 2, 7]
})

result = ventas.groupby('Producto')['Precio'].mean()
result_qity = ventas.groupby('Producto')['Unidades'].count()

print(result)
print(result_qity)


# 2
clientes = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Nombre': ['Ana', 'Luis', 'Marta', 'Carlos', 'Sofía'],
    'Ciudad': ['Lima', 'Arequipa', 'Lima', 'Cusco', 'Lima'],
    'Edad': [25, 30, 22, 35, 28]
})

sub_set = clientes.iloc[1:4]
print(sub_set[['Nombre', 'Ciudad']])

clientes.loc[clientes['Ciudad'] == 'Lima', 'Ciudad'] = 'Lima Metropolitana'
clientes.loc[clientes['Edad'] > 30, 'Edad'] = '30+'
print(clientes)
