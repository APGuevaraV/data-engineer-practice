import pandas as pd
import numpy as np

clientes = pd.DataFrame({
    'ID_Cliente': [101, 102, 103, 104, 105, 106, 107],
    'Nombre': ['Ana', 'Freddy', 'Lucía', 'Sandra', 'Pedro', 'Pablo', 'Erick'],
    'Edad': [29, 30, 27, 25, 31, 35, 23],
    'Ciudad': ['Trujillo', 'Lima', 'Trujillo', 'Chiclayo', 'Tacna',
               'Arequipa', 'Tumbes'],
    'Estado_Cuenta': ['activo', 'activo', 'inactivo', 'activo', 'activo',
                      'activo', 'inactivo'],
    'Deuda': [200, 12.5, 6, 600, 5.6, 2850, np.nan],
})

print(clientes.shape)
activos = len(clientes[clientes['Estado_Cuenta'] == 'activo'])
print(f"Activos : {activos}")
nulos_Deuda = len(clientes[clientes['Deuda'].isnull()])
print(f"Nulos en deuda : {nulos_Deuda}")
print(clientes.columns)
clientes['Edad'] = clientes['Edad'].astype(float)
porcentaje = (len(clientes[clientes['Deuda'] > 1000]) / clientes.shape[0])*100
print(round(porcentaje, 2))
