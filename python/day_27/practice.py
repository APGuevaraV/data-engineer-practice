import pandas as pd


df = pd.DataFrame({
    "Empleado": ["Ana", "Luis", "Marta", "Pedro", "Luis", "Ana"],
    "Ventas": [1000, 1500, 1200, 800, 600, 2000],
    "Region": ["Lima", "Cusco", "Lima", "Trujillo", "Lima", "Cusco"],
    "Año": [2024, 2024, 2025, 2025, 2024, 2025]
})

df_new = df.assign(
    Bonus=lambda x: x['Ventas']*0.1
)

print(df_new)

df['total ventas'] = df.groupby('Region')['Ventas'].transform('sum')
print(df)

subset = df.query("Ventas > 1000 and Año== 2025")
print(subset)


def categoria(ventas):
    if ventas > 1500:
        return 'Alto'
    elif 1000 <= ventas <= 1500:
        return 'Medio'
    else:
        return 'Bajo'


df['Categoria'] = df['Ventas'].apply(
    lambda x: categoria(x)
)
print(df)

df_new = df.assign(
    Bonus=lambda x: x['Ventas']*0.1
)
print(df_new.query("Region =='Lima' "))
