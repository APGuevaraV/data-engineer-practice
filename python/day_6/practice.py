productos = [
    {"id": 1, "nombre": "Laptop Lenovo Ideapad 5", "precio": 2500,
     "stock": 10},
    {"id": 2, "nombre": "Smartphone Samsung Galaxy S22", "precio": 3500,
     "stock": 5},
    {"id": 3, "nombre": "Tablet Apple iPad Air", "precio": 3000, "stock": 8},
    {"id": 4, "nombre": "Monitor LG UltraWide 29", "precio": 1200, "stock": 3},
    {"id": 5, "nombre": "Mouse Logitech MX Master 3", "precio": 450,
     "stock": 15}
]

n = int(input('ingrese el numero a buscar:'))

result = [print(x) for x in productos if x['id'] == n]
if not result:
    print('No encontrado')
