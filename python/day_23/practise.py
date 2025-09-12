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
