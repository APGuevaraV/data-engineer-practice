import pandas as pd

df = pd.DataFrame({
    'categoria': ['Electrónica', 'Electrónica', 'Hogar', 'Hogar', 'Ropa',
                  'Ropa', 'Electrónica'],
    'producto': ['Laptop', 'Mouse', 'Silla', 'Mesa', 'Camisa', 'Pantalón',
                 'Monitor'],
    'cantidad': [5, 20, 10, 4, 15, 8, 6],
    'precio_unitario': [3500, 50, 300, 500, 80, 120, 900]
})

df['total_ventas'] = df['cantidad']*df['precio_unitario']
filtered = df[df['total_ventas'] > 5000]
print(filtered)

pivote = pd.pivot_table(df, values=['cantidad', 'precio_unitario'], index=[
                        'categoria'], aggfunc={'cantidad': 'count',
                                               'precio_unitario': 'sum'})
print(pivote)
