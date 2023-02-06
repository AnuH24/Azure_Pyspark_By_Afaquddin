from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import *

#using Rdd
spark=SparkSession.builder.appName("word_count").getOrCreate()
# words =spark.sparkContext.textFile("E:/words.txt")
# a=words.flatMap(lambda line: line.split(" "))
# b = a.map(lambda word: (word, 1))
# c = b.reduceByKey(lambda a,b: a+b)
# c.collect()

#using data frame
data= spark.read.text("E:/words.txt")
data.show(10,False)
wc= data.\
    select(explode(split(data.value, ' '))).alias('words').\
    groupBy('words').\
    count()
wc.show()