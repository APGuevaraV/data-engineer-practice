empleados = [
    {"id": 1, "nombre": "Carlos Perez", "sueldo": 3800,
     "departamento": "Ventas"},
    {"id": 2, "nombre": "Lucía Fernández",
        "sueldo": 4500, "departamento": "Marketing"},
    {"id": 3, "nombre": "José Martínez", "sueldo": 5000,
     "departamento": "Finanzas"},
    {"id": 4, "nombre": "María López", "sueldo": 3200,
     "departamento": "Soporte"},
    {"id": 5, "nombre": "Ana Gómez", "sueldo": 4700,
        "departamento": "Recursos Humanos"},
    {"id": 6, "nombre": "Pedro Sánchez", "sueldo": 3900,
     "departamento": "TI"},
    {"id": 7, "nombre": "Sofía Torres", "sueldo": 5200,
     "departamento": "Logística"}
]

filtered = filter(lambda empleado: empleado['sueldo'] > 4000, empleados)
result = list(filtered)
for x in result:
    print(
        f"ID - {x['id']} - {x['nombre']} - {x['sueldo']} - {x['departamento']}")
