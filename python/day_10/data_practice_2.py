import numpy as np
import pandas as pd

ventas = pd.DataFrame({
    'Producto': ['Laptop', 'Celular', 'Tablet', 'Laptop', 'Tablet'],
    'Precio': [3500, 1500, 2200, 3700, 2100],
    'Unidades': [3, 10, 5, 2, 7]
})

filtered = ventas[(ventas['Producto'] == 'Laptop') & (ventas['Unidades'] > 2)]
print(filtered)

print(filtered[['Producto', 'Precio']])

ventas['Categoría Precio'] = 'Bajo'
ventas.loc[ventas['Precio'] >= 3000, 'Categoría Precio'] = 'Alto'
ventas.loc[(ventas['Precio'] >= 2000) & (ventas['Precio']
           <= 2999), 'Categoría Precio'] = 'Medio'
print(ventas)

# otra forma de hacerlo
condiciones = [
    (ventas['Precio'] >= 3000),
    (ventas['Precio'] >= 2000) & (ventas['Precio'] < 3000)
]

categorias = ['Alto', 'Medio']

ventas['Categoría Precio'] = np.select(condiciones, categorias, default='Bajo')

print(ventas)
