# Databricks notebook source
# Importacion de librerias y funciones

from pyspark.sql.types import *
from pyspark.sql.functions import *

# COMMAND ----------

catalog = "catalog_dev"
schema = "golden"

# COMMAND ----------

# lectura de la data
df_valoracion_usuarios = spark.table("catalog_dev.silver.valoracion_usuarios")

# COMMAND ----------

df_valoracion_usuarios.display()

# COMMAND ----------

df_valoracion_updated = df_valoracion_usuarios.groupBy("sexo", "nombre_ciudad").\
    agg(sum(col("edad")).alias("suma_edad"),
        count(col("edad")).alias("cont_edad"))

# COMMAND ----------

# Escribir a nuestra capa gold
df_valoracion_updated.write.mode('overwrite').format(
    'delta').saveAsTable(f'{catalog}.{schema}.valoracion_usuarios')

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS catalog_dev.golden.clase4

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS catalog_dev.golden.clase4_v_csv

# COMMAND ----------

df_valoracion_updated.write.save(f'/Volumes/catalog_dev/golden/clase4')

# COMMAND ----------

df_valoracion_updated.write.mode('overwrite').format(
    'csv').save('/Volumes/catalog_dev/golden/clase4_v_csv')
