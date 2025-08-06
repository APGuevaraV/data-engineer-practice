import pandas as pd

precios = pd.Series([150, 299, 450, 120, 780, 310, 520],
                    index=['A', 'B', 'C', 'D', 'E', 'F', 'G'])

print(precios['B':'E'])
mayores = precios[precios > 300]
menores_500 = precios[precios <= 500]
print(mayores)
print(menores_500)

enero = pd.Series([10, 15, 20, 5], index=['Producto1',
                  'Producto2', 'Producto3', 'Producto4'])
febrero = pd.Series([12, 14, 18, 7], index=['Producto1',
                    'Producto2', 'Producto3', 'Producto4'])

suma_total = enero.add(febrero).sum()
print(suma_total)
diferencia = febrero.subtract(enero)
print(f"Diferencia :{diferencia}")

crecimiento_porcentual = (febrero.sum() - enero.sum())/enero.sum() * 100
print(f"crecimiento porcentual:{crecimiento_porcentual}")


##
codigos = pd.Series(['001', '002', '003', '004'])
enteros = codigos.astype(int)
print(enteros)

flotantes = codigos.astype('float')
print(flotantes)
codigos = codigos.astype('string')
codigos_s = 'PROD-'+codigos
print(codigos_s)

##
calificaciones = pd.Series([18, 12, 15, 14, 20, 9, 16, 11])
primeros_5 = calificaciones.iloc[:5]
print(primeros_5)
nuevas_notas = 1+calificaciones
print(nuevas_notas)
aprobados = calificaciones[calificaciones > 13]
print(aprobados)

##
sueldos = pd.Series(['1500', '2200', '1800', '2500', '3000', '1200'])
sueldo_enteros = sueldos.astype(int)
diez_porciento = (1+(10/100)) * sueldos.astype(float)
filtrados = diez_porciento[diez_porciento > 2000]
primeros_3 = diez_porciento[:3]
print(sueldo_enteros)
print(diez_porciento)
print(filtrados)
print(primeros_3)
