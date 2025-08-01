import pandas as pd

ventas = {
    'nombre': ['Ana', 'Luis', 'Carla', 'Pedro'],
    'sueldo': [2500, 3500, 4000, 2800],
}

df = pd.DataFrame(ventas)
df['nivel'] = 'Junior'
df.loc[df['sueldo'] >= 3000, 'nivel'] = 'Senior'
print(df)
por_nivel = df.groupby('nivel')['nombre'].count().reset_index()
print(por_nivel)
