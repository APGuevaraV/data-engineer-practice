import pandas as pd

# Dataset 1 - Estudiantes
estudiantes = [
    {"Nombre": "Ana", "Edad": 20, "Nota": 17},
    {"Nombre": "Luis", "Edad": 22, "Nota": 15},
    {"Nombre": "María", "Edad": 19, "Nota": 18},
    {"Nombre": "Pedro", "Edad": 21, "Nota": 14},
    {"Nombre": "Sofía", "Edad": 23, "Nota": 16}
]
df_estudiantes = pd.DataFrame(estudiantes)
print(df_estudiantes)
# Dataset 2 - Países
paises = [
    {"País": "Perú", "Capital": "Lima", "Población": 33_000_000},
    {"País": "Argentina", "Capital": "Buenos Aires", "Población": 45_000_000},
    {"País": "Chile", "Capital": "Santiago", "Población": 19_000_000},
    {"País": "México", "Capital": "Ciudad de México", "Población":
        126_000_000},
    {"País": "España", "Capital": "Madrid", "Población": 47_000_000},
    {"País": "Colombia", "Capital": "Bogotá", "Población": 51_000_000}
]
df_paises = pd.DataFrame(paises)
print(df_paises)

# Dataset 3 - Productos
productos = [
    {"Producto": "Laptop", "Precio": 3500, "Stock": 10},
    {"Producto": "Mouse", "Precio": 50, "Stock": 150},
    {"Producto": "Teclado", "Precio": 120, "Stock": 80},
    {"Producto": "Monitor", "Precio": 800, "Stock": 30},
    {"Producto": "Impresora", "Precio": 450, "Stock": 20}
]
df_productos = pd.DataFrame(productos)
df_productos.rename(columns={'Stock': 'Inventario'}, inplace=True)
print(df_productos)
df_final = df_productos.loc[df_productos['Precio'] > 100]

# Dataset 4 - Ciudades
ciudades = [
    {"Ciudad": "Lima", "Temperatura": 19},
    {"Ciudad": "Buenos Aires", "Temperatura": 16},
    {"Ciudad": "Santiago", "Temperatura": 14},
    {"Ciudad": "Ciudad de México", "Temperatura": 21},
    {"Ciudad": "Madrid", "Temperatura": 18}
]
df_ciudades = pd.DataFrame(ciudades)
print('Mostrar solo la ciudad')
print(df_ciudades['Ciudad'])
print(df_ciudades.iloc[:3])

# Dataset 5 - Personas
personas = [
    {"Nombre": "Carlos", "Edad": 30, "Ciudad": "Lima"},
    {"Nombre": "Lucía", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Javier", "Edad": 35, "Ciudad": "Bogotá"},
    {"Nombre": "Fernanda", "Edad": 28, "Ciudad": "Buenos Aires"},
    {"Nombre": "Miguel", "Edad": 40, "Ciudad": "Santiago"}
]
df_personas = pd.DataFrame(personas)
df_result = df_personas.iloc[:4][['Nombre', 'Edad']]
print(df_result)

# Dataset 6 - Animales
animales = ["Perro", "Gato", "Loro", "Tortuga", "Caballo"]
tipos = ["Mamífero", "Mamífero", "Ave", "Reptil", "Mamífero"]
df_animales = pd.DataFrame({"Animal": animales, "Tipo": tipos})


serie = pd.Series(df_animales['Animal'])
print(serie)
print(type(serie))

print("\n10. df['Animal'] devuelve:", type(df_animales['Animal']))
print("    df[['Animal']] devuelve:", type(df_animales[['Animal']]))
