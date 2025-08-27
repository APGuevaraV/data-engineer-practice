import pandas as pd

from sqlalchemy import create_engine


# conexion
usuario = 'xxx'
password = 'xxxxxx.'
host = 'xxx'
puerto = 'xxxx'
base_datos = 'xxxxx'


try:
    engine = create_engine(
        f"mysql+pymysql://{usuario}:{password}@{host}:{puerto}/{base_datos}")

    data = {
        "nombre": ["Ana", "Luis", "Carla", "Pedro"],
        "edad": [25, 30, 28, 35],
        "area": ["TI", "Finanzas", "Marketing", "TI"],
        "salario": [3500, 4200, 3900, 4500]
    }
    df_empleados = pd.DataFrame(data)

    df_empleados.to_sql('employees5', con=engine,
                        if_exists='replace', index=False)
    print("DataFrame exportado a la tabla 'empleados'")

    df_mysql = pd.read_sql('SELECT * FROM employees5', con=engine)
    print(df_mysql)

except ConnectionError:
    print('error')
