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
