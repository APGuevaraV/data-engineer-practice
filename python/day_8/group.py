import pandas as pd

empleados = {
    'nombre': ['Ana', 'Pedro', 'Elena', 'Freddy', 'Paula'],
    'area': ['TI', 'Finanzas', 'TI', 'Ventas', 'Finanzas'],
    'sueldo': [4000, 3500, 4200, 3000, 3800]
}

df = pd.DataFrame(empleados)
sueldo_promedio_por_area = df.groupby('area')['sueldo'].mean()
# print(sueldo_promedio_por_area)

empleado_sueldo_maximo = df[df['sueldo'] == df['sueldo'].max()]
print(f"empleado sueldo máximo:{empleado_sueldo_maximo}")

empleados_por_area = df.groupby('area')['nombre'].count()
print(empleados_por_area)
