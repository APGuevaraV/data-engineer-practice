productos = [
    {"nombre": "Laptop Lenovo Ideapad 5", "categoria": "Tecnología"},
    {"nombre": "Smartphone Samsung Galaxy S22", "categoria": "Tecnología"},
    {"nombre": "Mesa de comedor", "categoria": "Hogar"},
    {"nombre": "Silla ergonómica", "categoria": "Hogar"},
    {"nombre": "Zapatillas Nike Air Max", "categoria": "Moda"},
    {"nombre": "Camisa de lino", "categoria": "Moda"},
    {"nombre": "Refrigeradora LG", "categoria": "Electrodomésticos"},
    {"nombre": "Microondas Samsung", "categoria": "Electrodomésticos"},
    {"nombre": "Audífonos Sony WH-1000XM4", "categoria": "Tecnología"},
    {"nombre": "Audífonos Sony WH-1000XM4", "categoria": "Casa"}
]

agrupados = {}
for x in productos:
    if x['categoria'] in agrupados:
        agrupados[x["categoria"]].append(x)

    else:
        agrupados[x["categoria"]] = [x]

for c, v in agrupados.items():
    print(c)
    print(v)
