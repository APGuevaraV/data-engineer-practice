import pandas as pd

data = {
    "Empleado": ["Ana", "Luis", "Ana", "Carlos", "Luis", "Ana", "Carlos"],
    "Departamento": ["Ventas", "Ventas", "Marketing", "Marketing", "Ventas",
                     "Marketing", "Marketing"],
    "Ventas": [500, 700, 300, 400, 600, 200, 100],
    "Año": [2022, 2022, 2022, 2022, 2023, 2023, 2023]
}

# Muestra las ventas totales por empleado y año,
# y ordénalas de mayor a menor dentro de cada año.

df = pd.DataFrame(data)
df_per_year = (
    pd.pivot_table(
        df,
        index="Empleado",
        columns="Año",
        values="Ventas",
        aggfunc="sum",
        fill_value=0
    )
)

df_per_year = df_per_year.sort_values(by=2022, ascending=False)
print(df_per_year)
