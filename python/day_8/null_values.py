from numpy import nan
import pandas as pd


workers = {
    'nombre': ['Juan', 'María', 'Pedro', 'Lucía'],
    'departamento': ['Ventas', nan, 'Finanzas', 'Marketing'],
    'sueldo': [2500, 2700, nan, 2800]
}

df = pd.DataFrame(workers)
nulos = df[df.isnull().any(axis=1)]
df_filled = df.fillna('Sin Asignar')
sueldo_promedio = round(df['sueldo'].mean(), 2)
print(sueldo_promedio)
df['sueldo'] = df['sueldo'].fillna(sueldo_promedio)
print(df)
