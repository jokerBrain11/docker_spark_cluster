# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col,date_format

# def init_spark():
#   sql = SparkSession.builder\
#     .appName("trip-app")\
#     .master("spark://spark-master:7077") \
#     .config("spark.jars", "/opt/spark-apps/postgresql-42.2.22.jar")\
#     .config("spark.driver.memory", "1G") \
#     .config("spark.executor.memory", "1G") \
#     .getOrCreate()
#   sc = sql.sparkContext
#   return sql,sc

# def main():
#   url = "jdbc:postgresql://demo-database:5432/mta_data"
#   properties = {
#     "user": "postgres",
#     "password": "password",
#     "driver": "org.postgresql.Driver"
#   }
#   file = "/opt/spark-data/y59h-w6v4_version_51.csv"
#   sql,sc = init_spark()

#   df = sql.read.load(file,format = "csv", inferSchema="true", sep=",", header="true") \
#       .withColumn("status[1]",col("state")[0]) \
#       # .withColumn("report_date",date_format(col("time_received"),"yyyy-MM-dd"))
  
#   # Filter invalid coordinates
#   # df.where("latitude <= 90 AND latitude >= -90 AND longitude <= 180 AND longitude >= -180") \
#   #   .where("latitude != 0.000000 OR longitude !=  0.000000 ") \
#   df.write \
#     .jdbc(url=url, table="mta_reports", mode='append', properties=properties) \
#     # .save()
  
# if __name__ == '__main__':
#   main()