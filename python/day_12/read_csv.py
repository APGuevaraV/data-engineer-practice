import pandas as pd

df = pd.read_csv('csv/ventas.csv')
ventas_by_category = df.groupby('categoria')['cantidad'].sum()
print(ventas_by_category)

df_empleados = pd.read_csv('csv/empleados.csv')
filtered_df = df_empleados[(df_empleados['departamento']
                           == 'IT') & (df_empleados['sueldo'] > 3800)]
print(filtered_df.sort_values(by='fecha_ingreso'))


# total de ventas por ciudad
df_pedidos = pd.read_csv('csv/pedidos.csv')
df_result = df_pedidos.groupby('ciudad').agg(

    total_ventas=('total', 'sum'),
    cantidad_pedidos=('id_pedido', 'count')

)

print(df_result)


df_inventario = pd.read_csv('csv/inventory.csv')
df_inventario['valor_total'] = df_inventario['precio']*df_inventario['stock']
filtered = df_inventario[df_inventario['valor_total'] > 10000]
print(filtered)


df_asistencia = pd.read_csv('csv/asistencia.csv')
total_dias = df_asistencia.groupby('empleado')['presente'].count()
dias_presentes = df_asistencia[df_asistencia['presente'] == 'Sí'].groupby('empleado')[
    'presente'].count()
porcentaje_asistencia = (dias_presentes / total_dias *
                         100).fillna(0).sort_values(ascending=False)
print("\nPorcentaje de asistencia por empleado:")
print(porcentaje_asistencia)
