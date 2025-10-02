# Databricks notebook source
data = [("Ana", 25), ("Luis", 30), ("María", 28)]
df = spark.createDataFrame(data, ["Nombre", "Edad"])

# Mostrar datos
df.show()

# COMMAND ----------
