import pandas as pd

df = pd.read_csv('ventas.csv')
ventas_by_category = df.groupby('categoria')['cantidad'].sum()
print(ventas_by_category)
