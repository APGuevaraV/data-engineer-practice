import pandas as pd

df = pd.read_csv('csv/inventory.csv')
# print(df)
# primera 3 columnas
print(df.head(3))
print(df.tail(5))
print('shape del df')
print(df.shape)
# tipos de datos
print(df.info())
print(df.describe(include='object'))
