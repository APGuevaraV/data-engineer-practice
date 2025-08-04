import pandas as pd


ventas = pd.DataFrame({
    'Producto': ['Laptop', 'Celular', 'Tablet', 'Laptop', 'Tablet'],
    'Precio': [3500, 1500, 2200, 3700, 2100],
    'Unidades': [3, 10, 5, 2, 7]
})

result = ventas.groupby('Producto')['Precio'].mean()
result_qity = ventas.groupby('Producto')['Unidades'].count()

print(result)
print(result_qity)
