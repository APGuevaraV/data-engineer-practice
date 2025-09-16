import pandas as pd

# Dataset A: Empleados
df_empleados = pd.DataFrame({
    "EmpleadoID": [1, 2, 3, 4, 5],
    "Nombre": ["Ana", "Luis", "Pedro", "María", "Lucía"],
    "Departamento": ["Ventas", "Ventas", "TI", "TI", "RRHH"],
    "Salario": [3000, 3500, 4000, 4200, 2800]
})

gb_dpto = df_empleados.groupby('Departamento')['Salario'].mean()
# print(gb_dpto)

# Dataset B: Proyectos
df_proyectos = pd.DataFrame({
    "ProyectoID": [101, 102, 103, 104],
    "NombreProyecto": ["Migración Cloud", "App Móvil", "Dashboard BI",
                       "Chatbot"],
    "Departamento": ["TI", "TI", "Ventas", "RRHH"]
})

# Dataset C: Asignaciones (Empleado-Proyecto)
df_asignaciones = pd.DataFrame({
    "EmpleadoID": [1, 2, 3, 3, 4, 5],
    "ProyectoID": [103, 103, 101, 102, 101, 104],
    "Horas": [40, 35, 50, 20, 30, 25]
})

df_join = pd.merge(
    df_empleados,
    df_asignaciones,
    how='inner',
    on='EmpleadoID'
)
df_join = pd.merge(df_join, df_proyectos,
                   how='inner',
                   on='ProyectoID')
print(df_join[['EmpleadoID', 'Departamento_x', 'ProyectoID', 'Horas']])
result = df_join[df_join['Horas'] > 30]
result.to_csv('csv/asignacion_horas.csv', encoding='utf-8', index=False)
print(result)
# Dataset D: Ventas mensuales
df_ventas_mensuales = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
    "Ana": [500, 700, 600, 650, 800],
    "Luis": [800, 900, 850, 950, 1000],
    "Pedro": [400, 450, 500, 550, 600]
})

pivote = df_ventas_mensuales.melt(
    id_vars=['Mes'],
    var_name='Empleado',
    value_name='Ventas'
)

print(pivote)

# Dataset E: Inventario
df_inventario = pd.DataFrame({
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Silla"],
    "Stock": [10, 200, 150, 50, 80],
    "PrecioUnitario": [3500, 40, 100, 800, 150]
})

df_inventario['CategoriaStock'] = df_inventario['Stock'].apply(
    lambda x:
        'Alto' if x > 100 else
        'Medio' if 50 <= x <= 100
        else 'Bajo'
)

print(df_inventario)
