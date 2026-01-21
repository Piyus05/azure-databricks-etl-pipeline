
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ETL").getOrCreate()

df = spark.read.csv("data/raw/sales.csv", header=True, inferSchema=True)
clean_df = df.dropDuplicates()
agg_df = clean_df.groupBy("product").sum("quantity")

agg_df.show()
