
inventario = {
    "Tecnología": [
        {"nombre": "Laptop Lenovo Ideapad 5", "stock": 10},
        {"nombre": "Smartphone Samsung Galaxy S22", "stock": 5},
        {"nombre": "Monitor LG UltraWide 29", "stock": 3}
    ],
    "Hogar": [
        {"nombre": "Mesa de comedor", "stock": 4},
        {"nombre": "Silla ergonómica", "stock": 6}
    ],
    "Moda": [
        {"nombre": "Zapatillas Nike Air Max", "stock": 12},
        {"nombre": "Camisa de lino", "stock": 8}
    ],
    "Electrodomésticos": [
        {"nombre": "Refrigeradora LG", "stock": 2},
        {"nombre": "Microondas Samsung", "stock": 5}
    ]
}

a = [
    {
        'categoria': c,
        'productos_totales': len(v),
        'stock_total': sum(producto['stock'] for producto in v)

    }
    for c, v in inventario.items()
]

print(a)
