import numpy as np
import pandas as pd

# Dataset
data = {
    'vendedor': ['Ana', 'Luis', 'Ana', 'Marcos', 'Luis', 'Ana', 'Marcos'],
    'categoria': ['Ropa', 'Calzado', 'Ropa', 'Accesorios', 'Ropa', 'Calzado',
                  'Accesorios'],
    'venta': [250, 400, 180, 120, 300, 150, 200],
    'fecha': pd.to_datetime(['2024-02-01', '2024-02-01', '2024-02-03',
                             '2024-02-05', '2024-02-06', '2024-02-10',
                             '2024-02-11'])
}

df = pd.DataFrame(data)

df_filtered = df[df['categoria'] == 'Ropa']
gb_df = df_filtered.groupby('vendedor')[['venta']].agg(
    {'venta': 'sum'}).sort_values(by='venta', ascending=False)
# print(gb_df)


data_2 = {
    'id': [1, 2, 3, 3, 4, 5, 6],
    'nombre': ['Ana', 'Luis', 'Marcos', 'Marcos', 'Elena', np.nan, 'Sofía'],
    'edad': [28, np.nan, 35, 35, 40, 30, 22],
    'salario': [2500, 3000, np.nan, np.nan, 4500, 3100, 2000]
}

df_employees = pd.DataFrame(data_2)
df_employees_clean = df_employees.drop_duplicates(
    subset=['id']).reset_index(drop=True)

df_employees_clean['edad'] = df_employees_clean['edad'].fillna(
    df_employees_clean['edad'].mean())

df_employees_clean['salario'] = df_employees_clean['salario'].fillna(
    df_employees_clean['salario'].median())

df_employees_clean_result = df_employees_clean[df_employees_clean['salario']
                                               > df_employees_clean['salario'].mean()]
# print(df_employees_clean_result)


data_3 = {
    'empleado': ['Ana', 'Luis', 'Marcos', 'Elena', 'Sofía'],
    'fecha_ingreso': pd.to_datetime(['2019-03-01', '2020-07-15', '2022-01-10', '2021-05-20', '2023-02-01']),
    'fecha_actual': pd.to_datetime(['2025-10-21'] * 5)
}

df_dates = pd.DataFrame(data_3)
df_diferencia = df_dates.assign(
    Años_servicio=lambda x: (x['fecha_actual'] - x['fecha_ingreso']).dt.days / 365.25)
df_diferencia['nivel_antiguedad'] = df_diferencia['Años_servicio'].apply(
    lambda x: 'Senior' if x >= 5 else
    'Semi-senior' if 2 <= x < 5
    else 'Junior'
)

result = df_diferencia[['empleado', 'Años_servicio', 'nivel_antiguedad']]
print(result)
# 2️⃣ Crea una columna "nivel_antiguedad" que clasifique:
#     - 'Senior' si años >= 5
#     - 'Semi-senior' si entre 2 y 4 años
#     - 'Junior' si < 2 años
# 3️⃣ Muestra solo las columnas empleado, años_servicio y nivel_antiguedad.
