# Databricks notebook source
# MAGIC %md
# MAGIC # Fundamentos de Apache Spark: Funciones avanzadas

# COMMAND ----------

# MAGIC %md
# MAGIC En este notebook aprenderemos algunas funciones avanzadas para optimizar el rendimiento de Spark, para imputar valores faltantes o a crear funciones definidas por el usuario (UDF).

# COMMAND ----------

#from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.functions import broadcast
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ### Crear el DataFrame

# COMMAND ----------

emp = [(1, "AAA", "dept1", 1000),
    (2, "BBB", "dept1", 1100),
    (3, "CCC", "dept1", 3000),
    (4, "DDD", "dept1", 1500),
    (5, "EEE", "dept2", 8000),
    (6, "FFF", "dept2", 7200),
    (7, "GGG", "dept3", 7100),
    (None, None, None, 7500),
    (9, "III", None, 4500),
    (10, None, "dept5", 2500)]

dept = [("dept1", "Department - 1"),
        ("dept2", "Department - 2"),
        ("dept3", "Department - 3"),
        ("dept4", "Department - 4")
       ]

df = spark.createDataFrame(emp, ["id", "name", "dept", "salary"])
deptdf = spark.createDataFrame(dept, ["id", "name"]) 

# Create Temp Tables
df.createOrReplaceTempView("empdf")
deptdf.createOrReplaceTempView("deptdf")

# Save as HIVE tables.
df.write.saveAsTable("hive_empdf", mode = "overwrite")
deptdf.write.saveAsTable("hive_deptdf", mode = "overwrite")

# COMMAND ----------

# MAGIC %md
# MAGIC ### BroadCast Join

# COMMAND ----------

# MAGIC %md
# MAGIC El tamaño de la tabla de difusión es de 10 MB. Sin embargo, podemos cambiar el umbral hasta 8GB según la documentación oficial de Spark 2.3.
# MAGIC
# MAGIC * Podemos verificar el tamaño de la tabla de transmisión de la siguiente manera:

# COMMAND ----------

size_str = spark.conf.get("spark.sql.autoBroadcastJoinThreshold")
size = int(size_str.replace("b", "")) / (1024 * 1024)

print("Default size of broadcast table is {0} MB.".format(size))

# COMMAND ----------

# MAGIC %md
# MAGIC * Podemos establecer el tamaño de la tabla de transmisión para que diga 50 MB de la siguiente manera:

# COMMAND ----------

spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 50 * 1024 * 1024)

# COMMAND ----------

size_str = spark.conf.get("spark.sql.autoBroadcastJoinThreshold")
size = int(size_str.replace("b", "")) / (1024 * 1024)

print("Default size of broadcast table is {0} MB.".format(size))

# COMMAND ----------

# Considere que necesitamos unir 2 Dataframes.
# small_df: DataFrame pequeño que puede caber en la memoria y es más pequeño que el umbral especificado.
# big_df: DataFrame grande que debe unirse con DataFrame pequeño.

join_df = df.join(broadcast(deptdf), df["dept"] == deptdf["id"])

# COMMAND ----------

# MAGIC %md
# MAGIC ### Almacenamiento en caché
# MAGIC Podemos usar la función de caché / persistencia para mantener el marco de datos en la memoria. Puede mejorar significativamente el rendimiento de su aplicación Spark si almacenamos en caché los datos que necesitamos usar con mucha frecuencia en nuestra aplicación.

# COMMAND ----------

df.cache()
df.count()
print("Memory Used : {0}".format(df.storageLevel.useMemory))
print("Disk Used : {0}".format(df.storageLevel.useDisk))

# COMMAND ----------

# MAGIC %md
# MAGIC Cuando usamos la función de caché, usará el nivel de almacenamiento como Memory_Only hasta Spark 2.0.2. Desde Spark 2.1.x es Memory_and_DISK.
# MAGIC
# MAGIC Sin embargo, si necesitamos especificar los distintos niveles de almacenamiento disponibles, podemos usar el método persist( ). Por ejemplo, si necesitamos mantener los datos solo en la memoria, podemos usar el siguiente fragmento.

# COMMAND ----------

from pyspark.storagelevel import StorageLevel

# COMMAND ----------

deptdf.persist(StorageLevel.MEMORY_ONLY)
deptdf.count()
print("Memory Used : {0}".format(df.storageLevel.useMemory))
print("Disk Used : {0}".format(df.storageLevel.useDisk))

# COMMAND ----------

# MAGIC %md
# MAGIC ### No persistir
# MAGIC También es importante eliminar la memoria caché de los datos cuando ya no sean necesarios.

# COMMAND ----------

df.unpersist()

# COMMAND ----------

sqlContext.clearCache()

# COMMAND ----------

# MAGIC %md
# MAGIC #  Expresiones SQL

# COMMAND ----------

# MAGIC %md
# MAGIC También podemos usar la expresión SQL para la manipulación de datos. Tenemos la función **expr** y también una variante de un método de selección como **selectExpr** para la evaluación de expresiones SQL.

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT *
# MAGIC FROM hive_empdf

# COMMAND ----------


# Intentemos categorizar el salario en Bajo, Medio y Alto según la categorización a continuación.

# 0-2000: salario_bajo
# 2001 - 5000: mid_salary
#> 5001: high_salary

cond = """case when salary > 5000 then 'high_salary'
               else case when salary > 2000 then 'mid_salary'
                    else case when salary > 0 then 'low_salary'
                         else 'invalid_salary'
                              end
                         end
                end as salary_level"""

newdf = df.withColumn("salary_level", expr(cond))
newdf.display()

# COMMAND ----------

newdf = df.withColumn(
    "salary_level",
    when(df.salary > 5000, 'high_salary')
    .when(df.salary > 2000, 'mid_salary')
    .when(df.salary > 0, 'low_salary')
    .otherwise('invalid_salary')
)

# Mostrar los primeros 5 registros
display(newdf.limit(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Usando la función selectExpr

# COMMAND ----------

newdf = df.selectExpr("*", cond)
newdf.display()

# COMMAND ----------

newdf = df.selectExpr("id","name", cond)
newdf.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Funciones definidas por el usuario (UDF)
# MAGIC A menudo necesitamos escribir la función en función de nuestro requisito muy específico. Aquí podemos aprovechar las udfs. Podemos escribir nuestras propias funciones en un lenguaje como python y registrar la función como udf, luego podemos usar la función para operaciones de DataFrame.
# MAGIC
# MAGIC * Función de Python para encontrar el nivel_salario para un salario dado.

# COMMAND ----------

def detSalary_Level(sal):
    level = None

    if(sal > 5000):
        level = 'high_salary'
    elif(sal > 2000):
        level = 'mid_salary'
    elif(sal > 0):
        level = 'low_salary'
    else:
        level = 'invalid_salary'
    return level

# COMMAND ----------

def lectura(ruta,tipo_dato):
    df = spark.read.format(tipo_dato).option("header","true").load(ruta)
    df.cache()
    return df

# COMMAND ----------

ruta = 'dbfs:/databricks-datasets/COVID/coronavirusdataset/PatientInfo.csv'
tipo_dato = 'csv'
lectura(ruta,tipo_dato).display()

# COMMAND ----------

# MAGIC %md
# MAGIC * Luego registre la función "detSalary_Level" como UDF.

# COMMAND ----------

sal_level = udf(detSalary_Level, StringType())

# COMMAND ----------

# MAGIC %md
# MAGIC * Aplicar función para determinar el salario_level para un salario dado.

# COMMAND ----------

df.display()

# COMMAND ----------

newdf = df.withColumn("salary_level", sal_level("salary"))
newdf.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Trabajando con valores NULL
# MAGIC
# MAGIC Los valores NULL siempre son difíciles de manejar independientemente del Framework o lenguaje que usemos. Aquí en Spark tenemos pocas funciones específicas para lidiar con valores NULL.
# MAGIC
# MAGIC - **es nulo()**
# MAGIC
# MAGIC Esta función nos ayudará a encontrar los valores nulos para cualquier columna dada. Por ejemplo si necesitamos encontrar las columnas donde las columnas id contienen los valores nulos.

# COMMAND ----------

newdf = df.filter(df["dept"].isNull())
newdf.display()

# COMMAND ----------

# MAGIC %md
# MAGIC * **No es nulo()**
# MAGIC
# MAGIC Esta función funciona de manera opuesta a la función isNull () y devolverá todos los valores no nulos para una función en particular.

# COMMAND ----------

newdf = df.filter(df["dept"].isNotNull())
newdf.display()

# COMMAND ----------

# MAGIC %md
# MAGIC * **fillna ()**
# MAGIC
# MAGIC Esta función nos ayudará a reemplazar los valores nulos.

# COMMAND ----------

# Replace -1 where the salary is null.
newdf = df.fillna("INVALID", ["dept"])
newdf.display()

# COMMAND ----------

# MAGIC %md
# MAGIC * **dropna ()**
# MAGIC
# MAGIC Esta función nos ayudará a eliminar las filas con valores nulos.

# COMMAND ----------

# Remove all rows which contains any null values.
newdf = df.dropna()
newdf.display()

# COMMAND ----------

# Elimina todas las filas que contienen todos los valores nulos.
newdf = df.dropna(how = "all")
newdf.display()

# Nota: valor predeterminado de "cómo" param es "any".

# COMMAND ----------

# Remove all rows where columns : dept is null.
newdf = df.dropna(subset = "dept")
newdf.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Partitioning
# MAGIC
# MAGIC
# MAGIC El particionamiento es un aspecto muy importante para controlar el paralelismo de la aplicación Spark.

# COMMAND ----------

# MAGIC %md
# MAGIC * Consultar número de particiones.

# COMMAND ----------

df.rdd.getNumPartitions()

# COMMAND ----------

# MAGIC %md
# MAGIC * Incrementar el número de particiones. Por ejemplo Aumentar las particiones a 6

# COMMAND ----------

newdf = df.repartition(6)
newdf.rdd.getNumPartitions()

# COMMAND ----------

# MAGIC %md
# MAGIC **Nota: se trata de operaciones costosas, ya que requiere la mezcla de datos entre los trabajadores.**

# COMMAND ----------

# MAGIC %md
# MAGIC * Disminuir el número de particiones. Por ejemplo disminuir las particiones a 2.

# COMMAND ----------

newdf = df.coalesce(2)
newdf.rdd.getNumPartitions()

# COMMAND ----------

# MAGIC %md
# MAGIC * De forma predeterminada, el número de particiones para Spark SQL es 200.
# MAGIC * Pero también podemos establecer el número de particiones en el nivel de aplicación Spark. Por ejemplo establecido en 500

# COMMAND ----------

# Set number of partitions as Spark Application.
spark.conf.set("spark.sql.shuffle.partitions", "500")

# Check the number of patitions.
num_part = spark.conf.get("spark.sql.shuffle.partitions")
print("No of Partitions : {0}".format(num_part))

# COMMAND ----------

# MAGIC %md
# MAGIC # Catálogo de APIs
# MAGIC
# MAGIC Spark Catalog es una API orientada al usuario, a la que puede acceder mediante SparkSession.catalog.

# COMMAND ----------

# MAGIC %md
# MAGIC * **listDatabases ()**
# MAGIC
# MAGIC Devolverá todas las bases de datos junto con su ubicación en el sistema de archivos.

# COMMAND ----------

spark.catalog.listDatabases()

# COMMAND ----------

# MAGIC %md
# MAGIC * **listTables ()**
# MAGIC
# MAGIC Devolverá todas las tablas para una base de datos determinada junto con información como el tipo de tabla (externa / administrada) y si una tabla en particular es temporal o permanente.
# MAGIC Esto incluye todas las vistas temporales.

# COMMAND ----------

spark.catalog.listTables("default")

# COMMAND ----------

# MAGIC %md
# MAGIC * **listColumns ()**
# MAGIC
# MAGIC Devolverá todas las columnas de una tabla en particular en DataBase. Además, devolverá el tipo de datos, si la columna se usa en particiones o agrupaciones.

# COMMAND ----------

spark.catalog.listColumns("hive_empdf", "default")

# COMMAND ----------

# MAGIC %md
# MAGIC * **listFunctions()**
# MAGIC
# MAGIC Devolverá todas las funciones disponibles en Spark Session junto con la información si es temporal o no.

# COMMAND ----------

spark.catalog.listFunctions()

# COMMAND ----------

# MAGIC %md
# MAGIC * **currentDatabase ()**
# MAGIC
# MAGIC Obtenga la base de datos actual.

# COMMAND ----------

spark.catalog.currentDatabase()

# COMMAND ----------

# MAGIC %md
# MAGIC * **setCurrentDatabase ()**
# MAGIC
# MAGIC Establecer la base de datos actual

# COMMAND ----------

spark.catalog.setCurrentDatabase("default")

# COMMAND ----------

# MAGIC %md
# MAGIC * **cacheTable ()**
# MAGIC
# MAGIC almacenar en caché una tabla en particular.
# MAGIC

# COMMAND ----------

spark.catalog.cacheTable("default.hive_empdf")

# COMMAND ----------

# MAGIC %md
# MAGIC * **isCached()**
# MAGIC
# MAGIC Compruebe si la tabla está almacenada en caché o no.

# COMMAND ----------

spark.catalog.isCached("default.hive_empdf")

# COMMAND ----------

# MAGIC %md
# MAGIC * **uncacheTable()**
# MAGIC
# MAGIC Des-cachear de una tabla en particular.

# COMMAND ----------

spark.catalog.uncacheTable("default.hive_empdf")

# COMMAND ----------

# Verify uncached table. Now you will see that it will return "False" which means table is not cached.
spark.catalog.isCached("default.hive_empdf")

# COMMAND ----------

# MAGIC %md
# MAGIC * **clearCache()**
# MAGIC
# MAGIC Des-cachear toda la tabla en la sesión de Spark.

# COMMAND ----------

spark.catalog.clearCache()