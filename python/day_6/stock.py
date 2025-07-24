productos = [
    {"nombre": "Laptop Lenovo Ideapad 5", "precio": 2500, "stock": 10},
    {"nombre": "Smartphone Samsung Galaxy S22", "precio": 3500, "stock": 3},
    {"nombre": "Tablet Apple iPad Air", "precio": 3000, "stock": 7},
    {"nombre": "Monitor LG UltraWide 29\"", "precio": 1200, "stock": 2},
    {"nombre": "Mouse Logitech MX Master 3", "precio": 450, "stock": 15},
    {"nombre": "Teclado Mecánico Razer", "precio": 800, "stock": 4},
    {"nombre": "Audífonos Sony WH-1000XM4", "precio": 1200, "stock": 8}
]

result = list(map(lambda x: x['nombre'], filter(
    lambda produ: produ['stock'] > 5, productos)))
print(f"Productos con stock mayor a 5 :{result}")
