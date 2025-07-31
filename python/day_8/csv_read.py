import pandas as pd


df = pd.read_csv('ventas.csv')
print(df)
# 5 primeros elementos del dataframa
print(df.head())
print(df['Unidades Vendidas'].sum())

df['Ingreso total'] = df['Precio']*df['Unidades Vendidas']
ingresos_por_categoria = df.groupby('Categoría')['Ingreso total'].sum()

print(ingresos_por_categoria)
