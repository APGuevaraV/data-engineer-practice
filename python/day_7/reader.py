
with open('productos.txt', 'r', encoding='utf8') as productos:
    for i, producto in enumerate(productos):
        print(f"{i+1} - {producto}")
