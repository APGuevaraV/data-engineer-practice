# Databricks notebook source
from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql.functions import udf, col

# COMMAND ----------

catalog = "catalog_dev"
schema = "silver"

# COMMAND ----------

# lectura de la data
df_valoracion_usuarios = spark.table("catalog_dev.bronze.valoracion_usuarios")
df_paciente = spark.table("catalog_dev.bronze.paciente")
df_ciudad = spark.table("catalog_dev.bronze.ciudad")

# COMMAND ----------

#creando vistas temporales para transformacion
df_valoracion_usuarios.createOrReplaceTempView("valoracion_usuarios_delta")
df_paciente.createOrReplaceTempView("paciente_delta")
df_ciudad.createOrReplaceTempView("ciudad_delta")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW VW_paciente AS (
# MAGIC
# MAGIC select 
# MAGIC
# MAGIC numero_de_identificacion,
# MAGIC `Tipo_de_identificación_del_usuario`,
# MAGIC concat(if(Primer_nombre_del_usuario is null or Primer_nombre_del_usuario = 'NONE','',concat(Primer_nombre_del_usuario,' ')),
# MAGIC        if(segundo_nombre_del_usuario is null,'',concat(segundo_nombre_del_usuario,' ')),
# MAGIC        if(Primer_apellido_del_usuario is null,'',concat(Primer_apellido_del_usuario,' ')), 
# MAGIC        if(segundo_apellido_del_usuario is null,'',segundo_apellido_del_usuario)
# MAGIC        ) as nombre_completo,
# MAGIC sexo,
# MAGIC edad,
# MAGIC peso,
# MAGIC ciudad
# MAGIC
# MAGIC from paciente_delta)

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from VW_paciente;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC --- tratamiento valoracion_usuarios_delta
# MAGIC
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW VW_valoracion_usuario AS (
# MAGIC
# MAGIC select 
# MAGIC
# MAGIC substr(fecha,1,10) AS fecha,
# MAGIC cedula,
# MAGIC TA_SIS,
# MAGIC DIABETICO,
# MAGIC HTA,
# MAGIC TABACO,
# MAGIC HDL,
# MAGIC CT,
# MAGIC DM
# MAGIC
# MAGIC from valoracion_usuarios_delta)

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from VW_valoracion_usuario

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC
# MAGIC --- Creando la sabana de la data
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW VW_valoracion_usuario_sabana AS (
# MAGIC select 
# MAGIC
# MAGIC vu.fecha,
# MAGIC vu.cedula,
# MAGIC vu.TA_SIS,
# MAGIC vu.DIABETICO,
# MAGIC vu.HTA,
# MAGIC vu.TABACO,
# MAGIC vu.HDL,
# MAGIC vu.CT,
# MAGIC vu.DM,
# MAGIC p.`Tipo_de_identificación_del_usuario` AS tipo_documento,
# MAGIC p.nombre_completo,
# MAGIC p.sexo,
# MAGIC p.edad,
# MAGIC p.peso,
# MAGIC c.nombre as nombre_ciudad
# MAGIC
# MAGIC
# MAGIC from VW_valoracion_usuario AS vu
# MAGIC
# MAGIC left join VW_paciente AS p
# MAGIC
# MAGIC on trim(p.numero_de_identificacion) = trim(vu.cedula)
# MAGIC
# MAGIC inner join ciudad_delta AS c
# MAGIC
# MAGIC on p.ciudad =  c.codigo )

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from VW_valoracion_usuario_sabana

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC
# MAGIC select
# MAGIC fecha,
# MAGIC cedula,
# MAGIC Tipo_documento,
# MAGIC nombre_completo,
# MAGIC sexo,
# MAGIC edad,
# MAGIC nombre_ciudad,
# MAGIC CASE
# MAGIC   WHEN puntuacion < 5 THEN "BAJO"
# MAGIC   WHEN puntuacion >= 5 AND puntuacion < 10 THEN "MODERADO"
# MAGIC   WHEN puntuacion >= 10 THEN "ALTO"
# MAGIC ELSE NULL
# MAGIC END AS RIESGO
# MAGIC
# MAGIC from
# MAGIC
# MAGIC (select
# MAGIC fecha,
# MAGIC cedula,
# MAGIC Tipo_documento,
# MAGIC nombre_completo,
# MAGIC sexo,
# MAGIC edad,
# MAGIC nombre_ciudad,
# MAGIC round((100 * (1 - 0.88936*exp(cal_edad + cal_CT - cal_HDL + cal_TA + cal_TABACO + cal_DM -23.9802 ))),2) AS puntuacion
# MAGIC
# MAGIC
# MAGIC
# MAGIC from
# MAGIC (select 
# MAGIC *,
# MAGIC (log(edad) * 3.06117) AS cal_edad,
# MAGIC (log(CT) * 1.12370) AS cal_CT,
# MAGIC (log(HDL) * 0.93263) AS cal_HDL,
# MAGIC (log(TA_SIS) * IF(HTA = "SI",1.99881,1.93303)) AS cal_TA,
# MAGIC (IF(TABACO = 'SI',0.65451,0)) AS cal_TABACO,
# MAGIC (IF(DM = 'SI',0.57367,0)) AS cal_DM
# MAGIC
# MAGIC
# MAGIC
# MAGIC from VW_valoracion_usuario_sabana))
# MAGIC

# COMMAND ----------

#Almacenado el resultado de nuestra query en un dataframe

query = """select
fecha,
cedula,
Tipo_documento,
nombre_completo,
sexo,
edad,
nombre_ciudad,
CASE
  WHEN puntuacion < 5 THEN "BAJO"
  WHEN puntuacion >= 5 AND puntuacion < 10 THEN "MODERADO"
  WHEN puntUacion >= 10 THEN "ALTO"
ELSE NULL
END AS RIESGO



from

(select
fecha,
cedula,
Tipo_documento,
nombre_completo,
sexo,
edad,
nombre_ciudad,
round((100 * (1 - 0.88936*exp(cal_edad + cal_CT - cal_HDL + cal_TA + cal_TABACO + cal_DM -23.9802 ))),2) AS puntuacion



from
(select 
*,
(log(edad) * 3.06117) AS cal_edad,
(log(CT) * 1.12370) AS cal_CT,
(log(HDL) * 0.93263) AS cal_HDL,
(log(TA_SIS) * IF(HTA = "SI",1.99881,1.93303)) AS cal_TA,
(IF(TABACO = 'SI',0.65451,0)) AS cal_TABACO,
(IF(DM = 'SI',0.57367,0)) AS cal_DM



from VW_valoracion_usuario_sabana))"""

df_VU = spark.sql(query)

# COMMAND ----------

df_VU.display()

# COMMAND ----------

#almacenando nuestra transformacion en nuestra capa silver
df_VU.write.mode('overwrite').format('delta').saveAsTable(f'{catalog}.{schema}.valoracion_usuarios')