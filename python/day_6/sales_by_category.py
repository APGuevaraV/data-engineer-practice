from functools import reduce

ventas = {
    "Tecnología": [1200, 850, 1500, 2000],
    "Moda": [400, 700, 550, 300],
    "Hogar": [600, 950, 300, 450],
    "Deportes": [800, 1200, 600, 700],
    "Electrodomésticos": [1300, 1700, 900, 1100]
}

total_sales_by_category = {}
for x in ventas.keys():
    total_sales_by_category[x] = reduce(lambda x, y: x+y, ventas[x])

print(total_sales_by_category)
