import pandas as pd

df = pd.read_csv('ventas.csv')
ventas_by_category = df.groupby('categoria')['cantidad'].sum()
print(ventas_by_category)

df_empleados = pd.read_csv('empleados.csv')
filtered_df = df_empleados[(df_empleados['departamento']
                           == 'IT') & (df_empleados['sueldo'] > 3800)]
print(filtered_df.sort_values(by='sueldo', ascending=False))


# total de ventas por ciudad
df_pedidos = pd.read_csv('pedidos.csv')
df_result = df_pedidos.groupby('ciudad').agg(
    {
        'total': 'sum',
        'ciudad': 'count'
    }
)

print(df_result)
