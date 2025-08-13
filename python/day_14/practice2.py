import pandas as pd

df = pd.DataFrame({
    'pais': ['Perú', 'Chile', 'Argentina', 'Perú', 'Brasil', 'Chile', 'Perú'],
    'producto': ['Café', 'Café', 'Azúcar', 'Azúcar', 'Café', 'Azúcar',
                 'Cacao'],
    'cantidad': [15, 20, 8, 30, 25, 5, 12],
    'precio_usd': [4, 4.2, 3, 3.5, 4.5, 3.2, 6]
})

filtered = df[(df['pais'].isin(['Perú', 'Chile']))
              & (df['producto'] == 'Café')]
print(filtered)
filtered_country = df[(df['pais'] != 'Perú') & (df['precio_usd'] > 4)]
print(filtered_country)
df['total_ud'] = df['precio_usd']*df['cantidad']

df = df[df['total_ud'] > 60]
print(df.reset_index())
