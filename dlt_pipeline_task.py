# Databricks notebook source
import dlt
from pyspark.sql.functions import col
@dlt.table(
    name="cars_raw",
    comment="Raw cars dataset loaded from the cars_volume"
)
def cars_raw():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load("/Volumes/workspace/default/cars_volume/Cars Datasets 2025.csv")
        .toDF(  
            "company_name",
            "car_name",
            "engine",
            "cc_battery_capacity",
            "horsepower",
            "total_speed",
            "performance_0_100_kmh",
            "price",
            "fuel_type",
            "seats",
            "torque"
        )
    )


@dlt.table(
    name="cars_clean",
    comment="Cleaned cars dataset with proper types"
)
def cars_clean():
    df = dlt.read("cars_raw")

    return (
        df.withColumn("price", col("price").cast("double"))  # ensure numeric type
          .dropna(subset=["company_name", "car_name", "price"])  # remove bad rows
    )


@dlt.table(
    name="cars_summary",
    comment="Average car price grouped by company_name"
)
def cars_summary():
    df = dlt.read("cars_clean")
    return (
        df.groupBy("company_name").avg("price")
          .withColumnRenamed("avg(price)", "avg_price")
          .orderBy(col("avg_price").desc())
    )


# COMMAND ----------

@dlt.table(
    name="cars_bronze",
    comment="Raw cars dataset as ingested"
)
def cars_bronze():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load("/Volumes/workspace/default/cars_volume/Cars Datasets 2025.csv")
        .toDF(
            "company_name",
            "car_name",
            "engine",
            "cc_battery_capacity",
            "horsepower",
            "total_speed",
            "performance_0_100_kmh",
            "price",
            "fuel_type",
            "seats",
            "torque"
        )
    )


# COMMAND ----------

@dlt.table(
    name="cars_silver",
    comment="Cleaned and standardized cars dataset"
)
@dlt.expect("valid_price", "price > 0")
@dlt.expect("valid_seats", "seats > 0")
def cars_silver():
    df = dlt.read("cars_bronze")

    return (
        df.withColumn("price", col("price").cast("double"))
          .dropna(subset=["company_name", "car_name", "price"])
          .dropDuplicates()
    )


# COMMAND ----------

@dlt.table(
    name="cars_gold",
    comment="Aggregated summary of average car price by company"
)
def cars_gold():
    df = dlt.read("cars_silver")
    return (
        df.groupBy("company_name")
          .avg("price")
          .withColumnRenamed("avg(price)", "avg_price")
          .orderBy(col("avg_price").desc())
    )


# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workspace.default.cars_bronze LIMIT 10;
# MAGIC SELECT * FROM workspace.default.cars_silver LIMIT 10;
# MAGIC SELECT * FROM workspace.default.cars_gold ORDER BY avg_price DESC;
# MAGIC