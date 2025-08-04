import pandas as pd

frutas = ['Manzana', 'Banana', 'Cereza', 'Durazno', 'Pera']

serie_frutas = pd.Series(frutas)
print(serie_frutas)
print(f"El primer elemento de la serie {serie_frutas[0]}")
print(f"Elemento cereza {serie_frutas[2]}")


capitales = {'Perú': 'Lima', 'Argentina': 'Buenos Aires',
             'Chile': 'Santiago', 'Colombia': 'Bogotá'}
serie_capitales = pd.Series(capitales)
print(serie_capitales)
print(serie_capitales.iloc[2])
print(serie_capitales.iloc[0])
print(serie_capitales['Chile'])
