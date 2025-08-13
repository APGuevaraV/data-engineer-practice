import pandas as pd

df = pd.DataFrame({
    'producto': ['Arroz', 'Azúcar', 'Aceite', 'Fideos', 'Leche', 'Pan'],
    'cantidad': [10, 5, 8, 12, 6, 15],
    'precio': [4.5, 3.8, 7.2, 2.5, 4.8, 1.2],
    'categoria': ['Granos', 'Granos', 'Aceites', 'Pastas', 'Lácteos',
                  'Panadería']
})

granos_products = df[df['categoria'] == 'Granos']
print(granos_products)

filtered_by_price = df[(df['precio'] > 4) & (df['cantidad'] > 8)]
print(filtered_by_price)

df['total_venta'] = df['cantidad'] * df['precio']
total_menor_20 = df[df['total_venta'] > 20]
print(total_menor_20)
