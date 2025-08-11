import pandas as pd

df = pd.read_csv('csv/productos.csv')

filtrado = df[(df['categoria'] == 'Tecnología') & (df['precio'] > 1500)]
print('\n Filtrados mayors a 1500 en Tecnología \n')
print(filtrado.reset_index())
print(filtrado.info())
print(filtrado.describe())
filtrado_ordered = filtrado.sort_values(by='precio', ascending=False)
