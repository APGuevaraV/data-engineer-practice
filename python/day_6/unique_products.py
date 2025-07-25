productos = [
    {"nombre": "Laptop Lenovo Ideapad 5", "precio": 2500},
    {"nombre": "Smartphone Samsung Galaxy S22", "precio": 3500},
    {"nombre": "Tablet Apple iPad Air", "precio": 3000},
    {"nombre": "Monitor LG UltraWide 29", "precio": 1200},
    {"nombre": "Laptop Lenovo Ideapad 5", "precio": 2500},
    {"nombre": "Mouse Logitech MX Master 3", "precio": 450},
    {"nombre": "Monitor LG UltraWide 29", "precio": 1200},
    {"nombre": "Teclado Mecánico Razer", "precio": 800},
    {"nombre": "Smartphone Samsung Galaxy S22", "precio": 3500}
]
unique_products = list(set(x['nombre'] for x in productos))
print(unique_products)
