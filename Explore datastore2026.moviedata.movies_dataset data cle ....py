# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import pandas as pd
import numpy as np

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM `datastore2026`.`moviedata`.`movies_dataset`;

# COMMAND ----------

movie_df = spark.sql("""select * from datastore2026.moviedata.movies_dataset""")
display(movie_df)

# COMMAND ----------

movie_df.printSchema()

# COMMAND ----------

movie_df.describe().display()

# COMMAND ----------

# display(sorted(movie_df.columns))
# movie_df.count()
display(movie_df.select('id').distinct().count())

# COMMAND ----------

movie_df_null = movie_df.select(*[count(when(col(c).isNull(), c)).alias(c) for c in movie_df.columns])
movie_df_null.display()

# COMMAND ----------

movie_df_check = movie_df.select('*').filter(movie_df.id.isNull())
movie_df_check.display()

# COMMAND ----------

movie_df_fill = movie_df.withColumn(
    "id",
    when(col("id").isNull(), (rand() * 1e9).cast("long")).otherwise(col("id"))
)
movie_df_fill.display()

# COMMAND ----------

movie_df = movie_df_fill
movie_df.display()

# COMMAND ----------

from functools import reduce

# COMMAND ----------

movie_df_check = movie_df.filter(
    reduce(lambda x,y: x | y, [movie_df[c].isNull() for c in movie_df.columns])
)
movie_df_check.display()


# COMMAND ----------

movie_df.printSchema()

# COMMAND ----------

not_null_id = movie_df.filter(col("id").isNotNull()) \
    .fillna({"vote_count": 0, "vote_average": 0, "popularity": 0})

# Rows where id is null: keep as is
null_id = movie_df.filter(col("id").isNull())

# Union both DataFrames
movie_df_change = not_null_id.unionByName(null_id)

display(movie_df_change)

# COMMAND ----------

movie_df=movie_df_change
display(movie_df)

# COMMAND ----------

movie_genre_df = movie_df.filter(col("id").
                                 isNotNull())\
                                     .fillna({"genre":"Not Available","overview":"Not Comments"})

display(movie_genre_df)

# COMMAND ----------

movie_genre_df.select('*').where((movie_genre_df.overview == "Not Comments")).display()

# COMMAND ----------

movie_df = movie_genre_df

# COMMAND ----------

movie_df_filled = movie_df.withColumn(
    "release_date_display",
    when(col("release_date").isNull(), "not yet released").otherwise(col("release_date").cast("string"))
)
display(movie_df_filled)

# COMMAND ----------

movie_df_filled.printSchema()

# COMMAND ----------

movie_df = movie_df_filled
display(movie_df)
movie_df = movie_df.withColumn("release_date", to_date(col("release_date"),"yyyy-MM-dd"))
display(movie_df)

# COMMAND ----------

movie_df.drop("release_date_display").display()

# COMMAND ----------

movie_df.write.format("delta").mode("overwrite").option("overwriteSchema",True).saveAsTable("datastore2026.moviedata.movies_dataset")

# COMMAND ----------


