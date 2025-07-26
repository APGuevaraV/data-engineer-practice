import csv

usuarios = [
    {"nombre": "Ana", "edad": 25, "email": "ana@example.com"},
    {"nombre": "Luis", "edad": 30, "email": "luis@example.com"},
    {"nombre": "María", "edad": 28, "email": "maria@example.com"}
]

with open('usuarios.csv', 'w', newline='\n', encoding='utf8') as csvfile:
    campos = ['nombre', 'edad', 'email']
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()
    for user in usuarios:
        writer.writerow({
            "nombre": user['nombre'],
            "edad": user['edad'],
            "email": user['email']
        })
