import pandas as pd

# Crear un DataFrame
data = {
    "nombre": ["Ana", "Luis", "Carla", "Pedro"],
    "edad": [25, 30, 28, 35],
    "area": ["TI", "Finanzas", "Marketing", "TI"],
    "salario": [3500, 4200, 3900, 4500]
}
df = pd.DataFrame(data)

df.to_csv("empleados.csv", index=False)
print("Archivo empleados.csv creado")
# Exportar a JSON
df.to_json("json/empleados.json", orient="records", lines=True)
print("Archivo empleados.json creado")

df_cvs = pd.read_csv('empleados.csv', encoding='utf8')
print(df_cvs)

df_json = pd.read_json('json/empleados.json', orient='records', lines=True)
df_high_salary = df_json[df_json['salario'] > 4000]
print(df_high_salary.reset_index())

nuevo = {'nombre': 'Sofía',
         'edad': 27,
         'area': 'RRHH',
         'salario': 4000}
df = df._append(nuevo, ignore_index=True)
print(df)

df.to_csv('empleados.csv', index=False)
df.to_json('json/empleados.json', orient='records',
           lines=True)

nombre_salario = pd.read_csv('empleados.csv', usecols=['nombre', 'salario'])
print(nombre_salario)

nombre_salario.sort_values(
    by='salario', ascending=False, inplace=True)

print(nombre_salario)

nombre_salario.to_csv('empleados_ordenados.csv', encoding='utf8')
