import pandas as pd

df = pd.DataFrame({
    'producto': ['Arroz', 'Azúcar', 'Aceite', 'Fideos', 'Leche', 'Pan'],
    'cantidad': [10, 5, 8, 12, 6, 15],
    'precio': [4.5, 3.8, 7.2, 2.5, 4.8, 1.2],
    'categoria': ['Granos', 'Granos', 'Aceites', 'Pastas', 'Lácteos',
                  'Panadería']
})

granos_products = df[df['categoria'] == 'Granos']
print(granos_products)

filtered_by_price = df[(df['precio'] > 4) & (df['cantidad'] > 8)]
print(filtered_by_price)

df['total_venta'] = df['cantidad'] * df['precio']
total_menor_20 = df[df['total_venta'] > 20]
print(total_menor_20)


df_employees = pd.DataFrame({
    'nombre': ['Luis', 'Ana', 'Pedro', 'Lucía', 'Carlos', 'Elena'],
    'departamento': ['IT', 'Marketing', 'IT', 'RRHH', 'IT', 'Marketing'],
    'sueldo': [3500, 2700, 4000, 2500, 3900, 2800],
    'edad': [28, 32, 26, 45, 30, 29]
})

print('\n Empleado:\n')
salary_upper_3700 = df_employees[df_employees['sueldo'] > 3700]
filtered_employees = salary_upper_3700[(salary_upper_3700['edad'] < 30) & (
    salary_upper_3700['departamento'] != 'RRHH')]
filtered_employees.drop('edad', axis=1)
print(filtered_employees.reset_index())


df_inventory = pd.DataFrame({
    'id_producto': [101, 102, 103, 104, 105, 106],
    'nombre': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora', 'USB'],
    'stock': [15, 50, 40, 8, 12, 100],
    'precio_unitario': [3500, 50, 120, 900, 600, 25]
})

filtered_inv = df_inventory[df_inventory['stock'] > 20]
fp = df_inventory[(df_inventory['precio_unitario'] > 500) & (
    df_inventory['stock'] > 10)]

df_inventory['total_venta'] = df_inventory['stock'] * \
    df_inventory['precio_unitario']
print(df_inventory)


df_pedidos = pd.DataFrame({
    'pedido_id': [1, 2, 3, 4, 5, 6],
    'cliente': ['Juan', 'María', 'Pedro', 'Lucía', 'Carlos', 'Ana'],
    'cantidad': [3, 1, 5, 2, 4, 1],
    'precio_unitario': [15, 50, 10, 30, 12, 200],
    'estado': ['Entregado', 'Pendiente', 'Entregado', 'Entregado', 'Pendiente',
               'Entregado']
})

ped_fil = df_pedidos[(df_pedidos['cantidad'] > 2) &
                     (df_pedidos['estado'] == 'Entregado')]
print(ped_fil)
ped_may_4 = df_pedidos[(df_pedidos['precio_unitario'] > 20)
                       & (df_pedidos['cantidad'] > 4)]

print(ped_may_4)
df_pedidos = df_pedidos.drop('estado', axis=1)
print(df_pedidos.head())
