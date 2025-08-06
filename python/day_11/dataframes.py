import pandas as pd

data = {
    'Nombre': ['Luis', 'Ana', 'Pedro', 'Lucía', 'Carlos', 'Elena'],
    'Departamento': ['IT', 'Marketing', 'IT', 'RRHH', 'IT', 'Marketing'],
    'Sueldo': ['3500', '2700', '4000', '2500', '3900', '2800'],
    'Edad': [28, 32, 26, 45, 30, 29]
}

df = pd.DataFrame(data)
df['Sueldo'] = df['Sueldo'].astype('int64')
print(df.dtypes)

filtered_employees = df[(df['Departamento'] == 'IT') & (df['Sueldo'] > 3800)]
print(filtered_employees)

df['Sueldo Neto'] = df['Sueldo'] * (1-(12/100))
print(df)

df['Categoria Edad'] = df['Edad'].apply(
    lambda x: 'Junior' if x < 30 else 'Senior')


df.sort_values('Sueldo Neto', inplace=True, ascending=False)

final = df[['Nombre', 'Departamento', 'Sueldo Neto', 'Categoria Edad']]
print(final)
