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


# Cursos y notas
df2 = pd.DataFrame({
    "curso": ["Python", "Python", "SQL", "SQL", "Excel", "Excel", "Python",
              "SQL"],
    "profesor": ["Juan", "Ana", "Juan", "Ana", "Ana", "Juan", "Juan", "Ana"],
    "nota": [15, 18, 11, 20, 14, 16, 19, 12],
    "asistencia": [12, 14, 9, 15, 13, 10, 16, 8]
})

by_notes = df2.groupby(['curso', 'profesor']).agg(
    maximo_notas=('nota', 'max'),
    minimo_asistencia=('asistencia', 'min'),
    promedio=('nota', lambda x: round(x.mean()))
).reset_index()
print(by_notes)

# producción de fábrica
df3 = pd.DataFrame({
    "fabrica": ["A", "A", "A", "B", "B", "C", "C", "C"],
    "turno": ["mañana", "tarde", "noche", "mañana", "tarde", "mañana",
              "tarde", "noche"],
    "unidades": [200, 180, 220, 150, 170, 300, 280, 310],
    "defectuosos": [5, 7, 6, 4, 8, 10, 9, 11]
})

production = df3.groupby(['fabrica', 'turno']).agg(
    suma_unidades=('unidades', 'sum'),
    porc_defectuoso=('defectuosos', lambda x: (
        x/df3.loc[x.index, 'unidades']).mean()),
    media=('unidades', lambda y: y.mean() if y.mean() > 200 else 0)
)
print(production)


df4 = pd.DataFrame({
    "cliente": ["A1", "A1", "B2", "B2", "C3", "C3", "C3", "A1"],
    "categoria": ["Electrónica", "Ropa", "Electrónica", "Ropa", "Electrónica",
                  "Ropa", "Ropa", "Ropa"],
    "monto": [500, 200, 700, 100, 300, 250, 400, 150],
    "items": [1, 2, 3, 1, 2, 1, 4, 1]
})

by_clients = df4.groupby(['cliente', 'categoria']).agg(
    gasto_total=('monto', 'sum'),
    nro_items=('items', 'sum'),
    ticket_promedio=('monto', lambda x: (
        x/df4.loc[x.index, 'items']).mean().round())
).reset_index()
print(by_clients)
