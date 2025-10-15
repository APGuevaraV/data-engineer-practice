# Databricks notebook source
#Importacion de librerias y funciones

from pyspark.sql.types import *
from pyspark.sql.functions import *

# COMMAND ----------

#Path de la data a tratar
valoracion_usuarios_data = "/Volumes/catalog_dev/raw/valoracion/valoracion_usuarios.csv"
ciudad_data = "/Volumes/catalog_dev/raw/ciudad/ciudad.csv"
paciente_data = "/Volumes/catalog_dev/raw/paciente/paciente.csv"

# COMMAND ----------

#Esquema valoracion usuarios
valoracion_usuarios_schema= StructType([
StructField('fecha',StringType(),nullable=True ),
StructField('cedula',StringType(),nullable=True),
StructField('TA_SIS',IntegerType(),nullable=True),
StructField('DIABETICO',StringType(),nullable=True),
StructField('HTA',StringType(),nullable=True),
StructField('TABACO',StringType(),nullable=True),
StructField('HDL',IntegerType(),nullable=True),
StructField('CT',IntegerType(),nullable=True),
StructField('DM',StringType(),nullable=True)
])

# COMMAND ----------

#Esquema ciudad
ciudad_schema = StructType([
StructField('CODIGO',StringType(),nullable=True ),
StructField('NOMBRE',StringType(),nullable=True),
])

# COMMAND ----------

#Esquema paciente
paciente_schema = StructType([
StructField('Tipo_de_identificación_del_usuario',StringType(),nullable=True ),
StructField('Numero_de_Identificacion',StringType(),nullable=True),
StructField('Primer_apellido_del_usuario',StringType(),nullable=True),
StructField('Segundo_apellido_del_usuario',StringType(),nullable=True),
StructField('Primer_nombre_del_usuario',StringType(),nullable=True),
StructField('Segundo_nombre_del_usuario',StringType(),nullable=True),
StructField('Fecha_de_Nacimiento',StringType(),nullable=True),
StructField('Sexo',StringType(),nullable=True),
StructField('Edad',IntegerType(),nullable=True),
StructField('Peso',StringType(),nullable=True),
StructField('ciudad',StringType(),nullable=True),
])

# COMMAND ----------

# lectura de la data
df_valoracion_usuarios = spark.read.schema(valoracion_usuarios_schema).csv(valoracion_usuarios_data,header=True,sep=",")
df_paciente = spark.read.schema(paciente_schema).csv(paciente_data,header=True,sep=",")
df_ciudad = spark.read.schema(ciudad_schema).csv(ciudad_data,header=True,sep=",")

# COMMAND ----------

df_valoracion_usuarios.limit(5).display()
df_paciente.limit(5).display()
df_ciudad.limit(5).display()

# COMMAND ----------

catalog = "catalog_dev"
schema = "bronze"

# COMMAND ----------

#transformacion de la data formato delta y almacenamiento
df_valoracion_usuarios.write.mode('overwrite').format("delta").saveAsTable(f"{catalog}.{schema}.valoracion_usuarios")
df_paciente.write.mode('overwrite').format("delta").saveAsTable(f"{catalog}.{schema}.paciente")
df_ciudad.write.mode('overwrite').format("delta").saveAsTable(f"{catalog}.{schema}.ciudad")