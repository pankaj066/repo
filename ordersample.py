from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import pyspark.sql.functions as sf
#import pandas as pd

def getyear(year):
   aa=year[0:4]
   return aa;
def getmonth(year):
   aa=year[0:7]
   return aa;
def getdttype(dty):
    #print(dty)
    a=dty
    return a;

customSchema = StructType([StructField("order_id", IntegerType(), True), StructField("order_date", DateType(), True),
                           StructField("amount", DoubleType(),True), StructField("status", StringType(), True)])

spark=SparkSession.builder.master("local").getOrCreate()
csvfile = spark.read.format("csv").options(header='true').schema(customSchema).load("D:/sample data/orders.txt")

#csvfile.withColumn("year",date_format("order_date",'yyyy')).show(5)
df = csvfile.withColumn("year",getyear(csvfile["order_date"].cast("string"))).withColumn("month",getmonth(csvfile["order_date"].cast("string")))
#df.show(5)
#df.filter('status=="COMPLETE"').groupBy("month").agg({'amount':'sum'}).alias("monthly_amount")
    #print(df.dtypes

##df.printSchema
##bb = getdttype(df.dtypes)
#print(bb)
monthlydf = df.filter('status=="COMPLETE"').groupBy("month").agg(sf.sum('amount').alias("monthly_amt"))
#monthlydf.orderBy(monthlydf.'month',monthlydf.'monthly_amt'.desc)
#monthlydf.show(5)

    #dfpf = df.p

