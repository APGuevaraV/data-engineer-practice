ciudades = [
    "Lima",
    "Cusco",
    "La Paz",
    "Buenos Aires",
    "Los Angeles",
    "Londres",
    "Madrid",
    "Lisboa",
    "Barcelona",
    "Lambayeque",
    "Arequipa",
    "Luján"
]
min_cities = list(map(lambda y: y.lower(), filter(
    lambda x: x[0].lower() == 'l', ciudades)))
print(min_cities)
