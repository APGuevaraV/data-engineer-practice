import pandas as pd

# Dataset
data = {
    'vendedor': ['Ana', 'Luis', 'Ana', 'Marcos', 'Luis', 'Ana', 'Marcos'],
    'categoria': ['Ropa', 'Calzado', 'Ropa', 'Accesorios', 'Ropa', 'Calzado',
                  'Accesorios'],
    'venta': [250, 400, 180, 120, 300, 150, 200],
    'fecha': pd.to_datetime(['2024-02-01', '2024-02-01', '2024-02-03',
                             '2024-02-05', '2024-02-06', '2024-02-10',
                             '2024-02-11'])
}

df = pd.DataFrame(data)

df_filtered = df[df['categoria'] == 'Ropa']
gb_df = df_filtered.groupby('vendedor')[['venta']].agg(
    {'venta': 'sum'}).sort_values(by='venta', ascending=False)
print(gb_df)
