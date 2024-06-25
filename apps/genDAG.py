from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

def init_spark():
    conf = SparkConf().setAppName("trip-app").setMaster("spark://spark-master:7077")
    sc = SparkContext(conf=conf)
    return sc

def simple_spark_job(sc):
    spark = SparkSession(sc)
    data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
    df = spark.createDataFrame(data, ["Name", "Age"])
    
    # 一些转换操作
    df_filtered = df.filter(df.Age > 30)
    df_grouped = df_filtered.groupBy("Name").count()
    
    # 动作操作以触发计算
    result = df_grouped.collect()
    
    # 打印结果
    print(result)

if __name__ == "__main__":
    sc = init_spark()
    simple_spark_job(sc)
    
    # 等待查看 Spark UI
    input("Press Enter to exit...")
