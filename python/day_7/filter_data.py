import csv

with open('ventas.csv', 'r', newline='\n', encoding='utf8') as ventas:
    reader = csv.DictReader(ventas, delimiter=',')
    result = sum(int(venta['cantidad']) * float(venta['precio_unitario'])
                 for venta in reader
                 if int(venta['cantidad']) >= 3)

print(f'Total ventas: {result}')
