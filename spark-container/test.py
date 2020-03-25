from pyspark.sql import SparkSession

spark_builder = SparkSession.builder.master("local[*]")

spark = spark_builder.getOrCreate()

uri = "s3://predictive-services-data-staging/expirable/dpam/purchase_vectorized/de105ac0-835f-4ce3-be2b-86bd14c5a1c9/data/"

