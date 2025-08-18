import pandas as pd

df_ventas = pd.DataFrame({
    "id_venta": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "producto": ["Laptop", "Mouse", "Teclado", "Laptop", "Mouse", "Teclado",
                 "Monitor", "Laptop", "Mouse", "Monitor"],
    "cantidad": [1, 2, 1, 3, 5, 2, 1, 2, 4, 3],
    "precio_unitario": [4000, 50, 80, 4200, 55, 85, 900, 4100, 60, 950],
    "ciudad": ["Lima", "Lima", "Cusco", "Lima", "Cusco", "Cusco", "Arequipa",
               "Arequipa", "Lima", "Cusco"]
})

group_by_product = df_ventas.groupby('producto')
total_amount_by_product = group_by_product['cantidad'].sum()
print(total_amount_by_product)
promedio_by_product = group_by_product['precio_unitario'].mean()
print(promedio_by_product)


# exercise 2
df_clientes = pd.DataFrame({
    "id_cliente": [101, 102, 103, 104, 105, 106, 107, 108],
    "nombre": ["Ana", "Luis", "Carla", "Pedro", "Sofía", "Miguel", "Lucía",
               "Andrés"],
    "ciudad": ["Lima", "Lima", "Cusco", "Arequipa", "Lima", "Cusco",
               "Arequipa", "Cusco"],
    "compras": [5, 8, 2, 10, 6, 4, 7, 3],
    "gasto_total": [500, 1200, 250, 2000, 800, 450, 1500, 300]
})

by_city = df_clientes.groupby('ciudad')
customers_by_city = by_city['id_cliente'].count()
print(customers_by_city)
cost_by_city = by_city['gasto_total'].mean().round(2)
print(cost_by_city)


df_empleados = pd.DataFrame({
    "id_empleado": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "nombre": ["Ana", "Luis", "Carla", "Pedro", "Sofía", "Miguel", "Lucía",
               "Andrés", "Rosa", "Diego"],
    "departamento": ["Ventas", "Ventas", "IT", "IT", "Marketing", "Marketing",
                     "IT", "Ventas", "Marketing", "IT"],
    "sueldo": [3000, 3200, 5000, 4800, 4000, 4200, 5100, 3100, 3900, 5300],
    "años_experiencia": [2, 3, 5, 6, 4, 7, 8, 2, 5, 10]
})

by_department = df_empleados.groupby('departamento')
sueldo_promedio = by_department['sueldo'].mean().round(2)
sueldo_maximo = by_department["sueldo"].max()
anios_experience = by_department['años_experiencia'].sum()
print(sueldo_promedio)
print(sueldo_maximo)
print(anios_experience)


df_pedidos = pd.DataFrame({
    "id_pedido": [201, 202, 203, 204, 205, 206, 207, 208, 209],
    "cliente": ["Ana", "Luis", "Carla", "Pedro", "Sofía", "Miguel", "Lucía",
                "Andrés", "Carla"],
    "categoria": ["Electrónica", "Ropa", "Electrónica", "Ropa", "Electrónica",
                  "Hogar", "Ropa", "Hogar", "Ropa"],
    "monto": [1200, 200, 800, 350, 1500, 600, 450, 700, 400],
    "fecha": pd.to_datetime([
        "2024-01-10", "2024-01-15", "2024-02-20", "2024-02-25",
        "2024-03-05", "2024-03-10", "2024-03-15", "2024-04-01", "2024-04-05"
    ])
})

by_date = df_pedidos.groupby(df_pedidos['fecha'].dt.month)
pedidos_by_month = by_date['id_pedido'].count()

print(pedidos_by_month)
monto_total_by_month = by_date['monto'].sum()
print(monto_total_by_month)

df_tickets = pd.DataFrame({
    "id_ticket": [301, 302, 303, 304, 305, 306, 307, 308],
    "soporte": ["Ana", "Luis", "Carla", "Pedro", "Sofía", "Luis", "Carla",
                "Pedro"],
    "categoria": ["Red", "Software", "Hardware", "Software", "Red", "Red",
                  "Hardware", "Software"],
    "tiempo_resolucion_horas": [5, 2, 8, 4, 3, 6, 7, 2],
    "satisfaccion_cliente": [4, 5, 3, 4, 5, 3, 2, 5]
})

by_support = df_tickets.groupby('soporte')
time = by_support['tiempo_resolucion_horas'].mean()
print(time)
satisfaccion = by_support['satisfaccion_cliente'].mean()
print(satisfaccion)
resolve_tickets = by_support['id_ticket'].count()
print(resolve_tickets)


df_transacciones = pd.DataFrame({
    "id_transaccion": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "cliente": ["Ana", "Luis", "Ana", "Pedro", "Sofía", "Luis", "Ana", "Pedro",
                "Lucía", "Sofía", "Luis", "Lucía"],
    "categoria": ["Electrónica", "Ropa", "Ropa", "Hogar", "Electrónica",
                  "Hogar", "Ropa", "Electrónica", "Hogar", "Ropa",
                  "Electrónica", "Electrónica"],
    "monto": [1200, 200, 150, 600, 1800, 700, 250, 2200, 950, 300, 1400, 1100],
    "fecha": pd.to_datetime([
        "2024-01-05", "2024-01-12", "2024-01-20", "2024-02-10", "2024-02-15",
        "2024-02-25",
        "2024-03-05", "2024-03-12", "2024-03-20", "2024-04-02", "2024-04-10",
        "2024-04-15"
    ])
})

customer_category = df_transacciones.groupby(['cliente', 'categoria']).agg(
    monto_total=('monto', 'sum'),
    n_transacciones=('id_transaccion', 'count')
).reset_index()

top2_por_cliente = customer_category.sort_values(['cliente', 'monto_total'],
                                                 ascending=[True, False]) \
    .groupby('cliente') \
    .head(2)
print(top2_por_cliente)


df_proyectos = pd.DataFrame({
    "id_proyecto": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "equipo": ["A", "A", "B", "B", "C", "C", "A", "B", "C"],
    "lider": ["Ana", "Luis", "Ana", "Carla", "Pedro", "Sofía", "Luis", "Carla",
              "Pedro"],
    "horas": [100, 120, 90, 80, 150, 140, 110, 95, 160],
    "costo": [5000, 6000, 4500, 4000, 7000, 6800, 5500, 4200, 7200]
})

by_equip_leader = df_proyectos.groupby(['equipo', 'lider']).agg(
    total_horas=('horas', 'sum'),
    promedio_cost=('costo', 'mean')
)

by_equip_leader['ranking'] = by_equip_leader.groupby(level=0)['total_horas'] \
                                            .rank(method='dense',
                                                  ascending=False)
print(by_equip_leader.sort_values(['equipo', 'ranking']))
