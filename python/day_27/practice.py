import pandas as pd


df = pd.DataFrame({
    "Empleado": ["Ana", "Luis", "Marta", "Pedro", "Luis", "Ana"],
    "Ventas": [1000, 1500, 1200, 800, 600, 2000],
    "Region": ["Lima", "Cusco", "Lima", "Trujillo", "Lima", "Cusco"],
    "Año": [2024, 2024, 2025, 2025, 2024, 2025]
})

df_new = df.assign(
    Bonus=lambda x: x['Ventas']*0.1
)

print(df_new)
