from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark=SparkSession.builder.appName("test").getOrCreate()
df=spark.read.format("csv").options(delimiter = "|", header="True").load("E:\onboarding_file.csv")
a=df.select(df.columns[2])
# header =a.first()
# b = a.subtract(header)
a.show(truncate=False)
print(a)
#df.write.csv("E:/cnu/output_file.csv")
# df.repartition(1).write.csv("E:\output_file.csv")
#df.show(truncate=False)
print(type(a))