import pandas as pd


df1 = pd.DataFrame({
    "empleado": ["Ana", "Ana", "Luis", "Luis", "Carla", "Carla", "Ana",
                 "Luis"],
    "region": ["Norte", "Sur", "Norte", "Norte", "Sur", "Norte", "Norte",
               "Sur"],
    "ventas": [1200, 800, 950, 1100, 500, 700, 1300, 400],
    "comision": [120, 80, 95, 110, 50, 70, 130, 40]
})

agrupado = df1.groupby(['empleado', 'region']).agg(
    promedio_ventas=('ventas', 'mean'),
    suma_ventas=('comision', 'sum'),
    rango_ventas=('ventas', lambda x: x.max() - x.min()),
).reset_index()
print(agrupado)
