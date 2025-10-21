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
print(df_employees_clean_result)
