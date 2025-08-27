import pandas as pd

# Crear un DataFrame
data = {
    "nombre": ["Ana", "Luis", "Carla", "Pedro"],
    "edad": [25, 30, 28, 35],
    "area": ["TI", "Finanzas", "Marketing", "TI"],
    "salario": [3500, 4200, 3900, 4500]
}
df = pd.DataFrame(data)

df.to_csv("empleados.csv", index=False)
print("Archivo empleados.csv creado")
# Exportar a JSON
df.to_json("json/empleados.json", orient="records", lines=True)
print("Archivo empleados.json creado")
