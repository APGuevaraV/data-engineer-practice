import pandas as pd


datos_estudiantes = {
    'nombre': ['Juan', 'María', 'Pedro', 'Lucía'],
    'edad': [20, 22, 19, 21],
    'nota': [15.5, 18.0, 14.0, 17.3]
}

df = pd.DataFrame(datos_estudiantes)
df_filtered = df[df['nota'] > 15]
print(df_filtered)
