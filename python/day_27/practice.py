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


# DATAFRAME 2

df_empleados = pd.DataFrame({
    'Empleado': ['Ana', 'Luis', 'María', 'Pedro', 'Sofía', 'Jorge'],
    'Departamento': ['Ventas', 'Ventas', 'IT', 'IT', 'RRHH', 'Ventas'],
    'Salario': [2500, 3000, 4000, 4200, 2800, 3100],
    'Edad': [25, 30, 28, 35, 40, 27],
    'AñoIngreso': [2020, 2018, 2019, 2015, 2010, 2021]
})
# print(df_empleados)


df_bono = df_empleados.assign(
    Bono=lambda x: x.apply(
        lambda row: row['Salario']*0.1 if row['Departamento'] == 'Ventas'
        else row['Salario']*0.05, axis=1)
)
print(df_bono)

df_empleados['Salario promedio'] = df_empleados.groupby(
    'Departamento')['Salario'].transform('mean')
print(df_empleados)

df_empleados['Nivel'] = df_empleados['Edad'].apply(
    lambda x:
        'Junior' if x < 30 else
        'Senior' if 30 <= x <= 39
        else 'Experto'

)
print(df_empleados)
