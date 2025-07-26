numeros = [4, 7, 10, 23, 8, 15, 42]
mayores_diez = [x**2 for x in numeros if x > 10]
print(mayores_diez)


precios = {
    "Laptop": 1200,
    "Monitor": 300,
    "Teclado": 50,
    "Mouse": 30
}

result = {
    x: v*3.8
    for x, v in precios.items()
}
print(result)
