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
