import pandas as pd

data1 = {
    "vendedor": ["Ana", "Luis", "Carla", "Ana", "Luis", "Carla", "Ana",
                 "Luis"],
    "region": ["Norte", "Norte", "Sur", "Sur", "Norte", "Sur", "Sur",
               "Norte"],
    "ventas": [1200, 1500, 800, 600, 2000, 900, 750, 1800],
    "mes": ["Enero", "Enero", "Enero", "Febrero", "Febrero", "Febrero",
            "Marzo", "Marzo"]
}

df = pd.DataFrame(data1)
by_month = df.groupby(['region', 'mes']).agg(
    {'ventas': 'sum'}
)

print(by_month)
vendedor_plus = df.groupby('vendedor')['ventas'].sum()
print(vendedor_plus.idxmax())
