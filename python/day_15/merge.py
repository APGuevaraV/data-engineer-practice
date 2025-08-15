import pandas as pd

# ==========================
# EJERCICIO 1:
# Combinar inventario con precios
# ==========================
df_inventario = pd.DataFrame({
    "id_producto": [101, 102, 103, 104],
    "producto": ["Laptop", "Mouse", "Teclado", "Monitor"],
    "stock": [15, 100, 50, 20]
})

df_precios = pd.DataFrame({
    "id_producto": [101, 102, 104, 105],
    "precio_unitario": [3500, 50, 800, 200]
})
# Une ambos para obtener un DataFrame con producto, stock
# y precio_unitario (left join)
inventario_precios = df_inventario.merge(df_precios,
                                         how='left',
                                         on='id_producto')[['producto',
                                                            'stock',
                                                            'precio_unitario']]
print(inventario_precios)


# ==========================
# EJERCICIO 2:
# Ventas por empleado en dos años
# ==========================
df_ventas_2023 = pd.DataFrame({
    "id_empleado": [1, 2, 3],
    "ventas_2023": [25000, 30000, 18000]
})

df_ventas_2024 = pd.DataFrame({
    "id_empleado": [2, 3, 4],
    "ventas_2024": [32000, 21000, 15000]
})

df_empleados = pd.DataFrame({
    "id_empleado": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "Carla", "Jorge"]
})

ventas = pd.merge(df_ventas_2023, df_ventas_2024,
                  on='id_empleado',
                  how='outer')

ventas = pd.merge(ventas, df_empleados,
                  on='id_empleado',
                  how='outer')
print(ventas)


# ==========================
# EJERCICIO 3:
# Concatenar reportes trimestrales
# ==========================
df_trimestre1 = pd.DataFrame({
    "mes": ["Enero", "Febrero", "Marzo"],
    "ventas": [1000, 1200, 900]
})

df_trimestre2 = pd.DataFrame({
    "mes": ["Abril", "Mayo", "Junio"],
    "ventas": [1100, 1300, 1250]
})

df_trimestre3 = pd.DataFrame({
    "mes": ["Julio", "Agosto", "Septiembre"],
    "ventas": [1400, 1350, 1500]
})
# Concatena los tres DataFrames en uno solo y ordena
# por mes respetando el orden cronológico


def obtener_numero_mes(mes):
    meses = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
        'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
        'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    return meses.get(mes)


reporte = pd.concat([
    df_trimestre1,
    df_trimestre2,
    df_trimestre3],
    axis=0,
    ignore_index=True
)

reporte['mes_num'] = reporte['mes'].apply(
    lambda x: obtener_numero_mes(x.lower()))
reporte = reporte.sort_values(by='mes_num').reset_index(drop=True)

print(reporte[['mes', 'ventas']])


# ==========================
# EJERCICIO 4:
# Información de cursos y profesores
# ==========================
df_cursos = pd.DataFrame({
    "id_curso": [1, 2, 3],
    "curso": ["Python", "SQL", "Excel"]
})

df_profesores = pd.DataFrame({
    "id_curso": [1, 2, 4],
    "profesor": ["María", "Pedro", "Sofía"]
})
# Une para mostrar todos los cursos y, si no hay profesor asignado,
# que aparezca NaN

schedule = pd.merge(
    df_cursos,
    df_profesores,
    how='left',
    on='id_curso',
)

print(schedule)


# ==========================
# EJERCICIO 5:
# Datos de clientes de dos sistemas diferentes
# ==========================
df_clientes_sistemaA = pd.DataFrame({
    "id_cliente": [1, 2, 3],
    "nombre": ["Ana", "Luis", "Carla"],
    "ciudad": ["Lima", "Cusco", "Arequipa"]
})

df_clientes_sistemaB = pd.DataFrame({
    "id_cliente": [4, 5],
    "nombre": ["Jorge", "Lucía"],
    "ciudad": ["Piura", "Tacna"]
})
# Concatena ambos DataFrames en uno solo y resetea el índice
df_clientes_sistemaA['sistema'] = 'A'
df_clientes_sistemaB['sistema'] = 'B'
sistema = pd.concat(
    [df_clientes_sistemaA, df_clientes_sistemaB], axis=0, ignore_index=True)
print(sistema)
