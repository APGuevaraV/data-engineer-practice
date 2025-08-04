import numpy as np
import pandas as pd

numeros = np.arange(10, 60, 10)
print(numeros)
serie = pd.Series(numeros, index=['A', 'B', 'C', 'D', 'E'])
print(serie.iloc[2])
print(serie['C'])

dias = ['Lunes', 'Martes', 'Miércoles',
        'Jueves', 'Viernes', 'Sábado', 'Domingo']
serie_dias = pd.Series(dias, index=['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'])
print(serie_dias.iloc[2])
print(serie_dias['D3'])


suerte = [7, 13, 21, 33, 42, 56, 63]
serie_suerte = pd.Series(suerte)
primeros_tres = serie_suerte[:3]
ultimos_tres = serie_suerte[-3:]
cuarto = serie_suerte[3]
print(primeros_tres)
print(ultimos_tres)
print(cuarto)
