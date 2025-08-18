import pandas as pd

df_ventas = pd.DataFrame({
    "id_venta": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "producto": ["Laptop", "Mouse", "Teclado", "Laptop", "Mouse", "Teclado",
                 "Monitor", "Laptop", "Mouse", "Monitor"],
    "cantidad": [1, 2, 1, 3, 5, 2, 1, 2, 4, 3],
    "precio_unitario": [4000, 50, 80, 4200, 55, 85, 900, 4100, 60, 950],
    "ciudad": ["Lima", "Lima", "Cusco", "Lima", "Cusco", "Cusco", "Arequipa",
               "Arequipa", "Lima", "Cusco"]
})

group_by_product = df_ventas.groupby('producto')
total_amount_by_product = group_by_product['cantidad'].sum()
print(total_amount_by_product)
promedio_by_product = group_by_product['precio_unitario'].mean()
print(promedio_by_product)
