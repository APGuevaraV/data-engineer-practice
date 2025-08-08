import mysql.connector
import pandas as pd

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='AnaPaula125195.',
    database='test'
)

query = "SELECT * FROM clientes"
df = pd.read_sql_query(query, conexion)
print(df)
df_activos = df[df['activo'] == 1]
print(f"cantidad de usuarios activos: {len(df_activos)}")
