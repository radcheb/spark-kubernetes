from pyspark.sql import SparkSession

spark_builder = SparkSession.builder.master("local[*]")

spark = spark_builder.getOrCreate()

uri = "s3://path/to/data/"

df = spark.read.parquet(uri)

df