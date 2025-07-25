productos = [
    {"id": 1, "nombre": "Laptop Lenovo", "precio": 2500},
    {"id": 2, "nombre": "Smartphone Samsung", "precio": 3500},
    {"id": 3, "nombre": "Tablet iPad", "precio": 3000},
    {"id": 4, "nombre": "Monitor LG", "precio": 1200}
]

ventas = [
    {"producto_id": 1, "cantidad_vendida": 5},
    {"producto_id": 2, "cantidad_vendida": 3},
    {"producto_id": 4, "cantidad_vendida": 2}
]


def buscar_producto(producto_id: int):
    return next(p for p in productos if p['id'] == producto_id)


"""
result = list(map(lambda x: {
    'nombre_producto': buscar_producto(x['producto_id'])['nombre'],
    'precio_unitario': buscar_producto(x['producto_id'])['precio'],
    'cantidad_vendida': x['cantidad_vendida'],
    'ingreso_total': x['cantidad_vendida'] *
    buscar_producto(x['producto_id'])['precio']
}, ventas))
"""


result = []
for venta in ventas:
    producto = buscar_producto(venta['producto_id'])
    result.append({
        'nombre_producto': producto['nombre'],
        'precio_unitario': producto['precio'],
        'cantidad_vendida': venta['cantidad_vendida'],
        'ingreso_total': venta['cantidad_vendida'] * producto['precio']
    })
print(list(result))
