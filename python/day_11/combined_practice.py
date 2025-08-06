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

# Resumen Financiero
facturacion = pd.DataFrame({
    'ID_Cliente': [101, 102, 101, 105, 104],
    'Factura_ID': [1, 2, 3, 4, 5],
    'Monto': [3205, 521, 456, 1245, 539],
    'Impuesto': [0.18, 0.18, 0.12, 0.10, 0.18]
})

facturacion['Total Factura'] = facturacion['Monto']*(1+facturacion['Impuesto'])

facturado_por_cliente = facturacion.groupby(
    'ID_Cliente').agg({
        'Total Factura': 'sum'
    })

facturacion['Promedio facturado'] = facturacion.groupby(
    'ID_Cliente')['Total Factura'].transform('mean')

valores_nulos = len(facturacion[facturacion.isnull().any(axis=1)])

dimension = facturacion.shape
print(dimension)
print(valores_nulos)
print(facturacion)
