import pandas as pd

ventas = pd.DataFrame({
    'ID_Venta': [11, 12, 13, 14, 15, 16],
    'ID_Producto': [101, 102, 103, 104, 102, 101],
    'País': ['Perú', 'Colombia', 'Brasil', 'Uruguay', 'Chile', 'Canadá'],
    'Cantidad': [2, 3, 1, 5, 1, 3]
})

productos = pd.DataFrame({
    'ID_Producto': [101, 102, 103, 104, 105, 106, 107],
    'Nombre_Producto': ['Televisor', 'Celular', 'Laptop', 'Tablet',
                        'Audifonos', 'Mouse', 'Teclado'],
    'Precio': [1800, 1500, 2500, 899, 500, 120, 150]
})

left_join = pd.merge(ventas, productos, how='left', on='ID_Producto')
sin_producto = left_join[left_join['Nombre_Producto'].isnull()]
print(f"Ventas sin producto asociado :{len(sin_producto)}")
dimension = left_join.shape
print(f"Dimensión{dimension[0], dimension[1]}")
ventas_peru = left_join[left_join['País'] == 'Perú']
print(f"Ventas en Perú:{len(ventas_peru)}")
