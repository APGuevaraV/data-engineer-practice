import pandas as pd

data = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Silla",
                 "Escritorio", "Webcam"],
    "Categoría": ["Electrónica", "Electrónica", "Electrónica", "Electrónica",
                  "Muebles", "Muebles", "Electrónica"],
    "Precio": [4000, 80, 150, 1200, 700, 1500, 300],
    "Cantidad": [5, 20, 15, 8, 12, 6, 10]
}
df = pd.DataFrame(data)
df['Total ventas'] = df['Precio'] * df['Cantidad']
gb_base = df.groupby('Categoría')['Total ventas'].sum()
print(gb_base)


data = {
    "Estudiante": ["Ana", "Luis", "Carlos", "María", "Elena", "Pedro"],
    "Matemáticas": [15, 12, 18, 14, 16, 11],
    "Historia": [13, 17, 15, 16, 12, 14],
    "Inglés": [16, 14, 19, 13, 18, 15]
}
df_estudiantes = pd.DataFrame(data)
df_estudiantes['Promedio'] = df_estudiantes[[
    'Matemáticas', 'Historia', 'Inglés']].mean(axis=1)
df_estudiantes['Aprobado'] = df_estudiantes['Promedio'] >= 14
print(df_estudiantes)


data = {
    "Empleado": ["Juan", "Sofía", "Andrés", "Marta", "Pablo", "Lucía"],
    "Departamento": ["IT", "IT", "Ventas", "Ventas", "RRHH", "RRHH"],
    "Sueldo": [4500, 5000, 3000, 3200, 4000, 3800],
    "Años_Experiencia": [5, 8, 2, 4, 6, 3]
}
df_employees = pd.DataFrame(data)
gb_dpto = df_employees.groupby('Departamento')['Sueldo'].mean()
print(gb_dpto)
maximos = df_employees.loc[df_employees.groupby(['Departamento'])[
    'Sueldo'].idxmax()]
print(maximos)

data = {
    "Cliente": ["A", "B", "A", "C", "B", "C", "A"],
    "Producto": ["Leche", "Pan", "Queso", "Leche", "Queso", "Pan", "Pan"],
    "Precio": [5, 2, 10, 5, 10, 2, 2],
    "Cantidad": [2, 5, 1, 3, 2, 4, 6],
    "Fecha": pd.to_datetime(["2025-01-10", "2025-01-12", "2025-01-15",
                             "2025-02-01", "2025-02-03", "2025-02-04",
                             "2025-02-10"])
}
df_ventas = pd.DataFrame(data)
df_ventas['Total'] = df_ventas['Cantidad']*df_ventas['Precio']
grp = df_ventas.groupby('Cliente')['Total'].sum()
print(grp)

df_ventas['Mes'] = df_ventas['Fecha'].dt.to_period('M')
maximos = df_ventas.groupby('Mes')['Total'].sum()
print(maximos.idxmax())
