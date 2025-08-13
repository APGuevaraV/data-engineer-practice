import pandas as pd

df = pd.DataFrame({
    'producto': ['Arroz', 'Azúcar', 'Aceite', 'Fideos', 'Leche', 'Pan'],
    'cantidad': [10, 5, 8, 12, 6, 15],
    'precio': [4.5, 3.8, 7.2, 2.5, 4.8, 1.2],
    'categoria': ['Granos', 'Granos', 'Aceites', 'Pastas', 'Lácteos',
                  'Panadería']
})

granos_products = df[df['categoria'] == 'Granos']
print(granos_products)

filtered_by_price = df[(df['precio'] > 4) & (df['cantidad'] > 8)]
print(filtered_by_price)

df['total_venta'] = df['cantidad'] * df['precio']
total_menor_20 = df[df['total_venta'] > 20]
print(total_menor_20)


df_employees = pd.DataFrame({
    'nombre': ['Luis', 'Ana', 'Pedro', 'Lucía', 'Carlos', 'Elena'],
    'departamento': ['IT', 'Marketing', 'IT', 'RRHH', 'IT', 'Marketing'],
    'sueldo': [3500, 2700, 4000, 2500, 3900, 2800],
    'edad': [28, 32, 26, 45, 30, 29]
})

print('\n Empleado:\n')
salary_upper_3700 = df_employees[df_employees['sueldo'] > 3700]
filtered_employees = salary_upper_3700[(salary_upper_3700['edad'] < 30) & (
    salary_upper_3700['departamento'] != 'RRHH')]
filtered_employees.drop('edad', axis=1)
print(filtered_employees.reset_index())
