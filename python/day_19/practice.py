import pandas as pd

data1 = {
    "vendedor": ["Ana", "Luis", "Carla", "Ana", "Luis", "Carla", "Ana",
                 "Luis"],
    "region": ["Norte", "Norte", "Sur", "Sur", "Norte", "Sur", "Sur",
               "Norte"],
    "ventas": [1200, 1500, 800, 600, 2000, 900, 750, 1800],
    "mes": ["Enero", "Enero", "Enero", "Febrero", "Febrero", "Febrero",
            "Marzo", "Marzo"]
}

df = pd.DataFrame(data1)
by_month = df.groupby(['region', 'mes']).agg(
    {'ventas': 'sum'}
)

print(by_month)
vendedor_plus = df.groupby('vendedor')['ventas'].sum()
print(vendedor_plus.idxmax())

data2 = {
    "estudiante": ["Ana", "Luis", "Carla", "Pedro", "Ana", "Luis", "Carla",
                   "Pedro"],
    "curso": ["Matemáticas", "Matemáticas", "Matemáticas", "Matemáticas",
              "Historia", "Historia", "Historia", "Historia"],
    "nota": [15, 12, 18, 14, 17, 16, 19, 11],
    "grupo": ["A", "A", "B", "B", "A", "A", "B", "B"]
}

df2 = pd.DataFrame(data2)

prommedio = df2.groupby(['curso', 'grupo'])['nota'].mean()
print(prommedio)
por_estudiante = df2.groupby(['curso'])['nota'].idxmax()
resultado = df2.loc[por_estudiante, ['curso', 'estudiante', 'nota']]
print(resultado)
