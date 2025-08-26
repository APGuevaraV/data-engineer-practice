import pandas as pd

data = {
    "Empleado": ["Ana", "Ana", "Luis", "Luis", "Carla", "Carla", "Pedro", "Pedro"],
    "Departamento": ["Ventas", "Marketing", "Ventas", "Marketing", "Ventas", "Marketing", "Ventas", "Marketing"],
    "Mes": ["Enero", "Enero", "Enero", "Febrero", "Febrero", "Enero", "Febrero", "Febrero"],
    "Ventas": [2000, 1800, 2200, 2100, 2500, 2300, 1900, 1700],
    "Horas": [160, 150, 170, 165, 155, 145, 160, 150]
}

df = pd.DataFrame(data)
print(df)


by_employyee = pd.pivot_table(
    df, index="Empleado", values="Ventas", aggfunc="sum")
print(by_employyee)

depto_employee = pd.pivot_table(
    df, index="Empleado", columns="Departamento", values="Ventas", aggfunc="sum")
print(depto_employee)
