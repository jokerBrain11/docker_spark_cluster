# from pyspark import SparkContext, SparkConf
# from operator import add

# data_path = "/opt/spark-data"

# def init_spark():
#     conf = SparkConf().setAppName("trip-app").setMaster("spark://spark-master:7077")
#     sc = SparkContext(conf=conf)
#     return sc

# def main():
#     sc = init_spark()

#     rdd = sc.textFile(f"{data_path}/fakeData1.txt")
#     rdd = rdd.flatMap(lambda x: x.split("|"))
#     spliedRdd = rdd.map(lambda x: tuple(x.split(","))).cache()

#     sumRdd = spliedRdd.reduceByKey(lambda x, y: int(x) + int(y))
#     # sumRdd = spliedRdd.reduceByKey(lambda x, y: int(x) + int(y)).cache()

#     countRDD = spliedRdd.mapValues(lambda x: (int(x), 1)) \
#         .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

#     avgRdd = spliedRdd.mapValues(lambda x: (int(x), 1)) \
#         .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) \
#         .mapValues(lambda x: x[0] / x[1])
    
#     print("各ID的值加總")
#     print(sumRdd.collect())
#     print("各ID的總比數")
#     print(countRDD.collect())
#     print("各ID的值平均")
#     print(avgRdd.collect())

# if __name__ == '__main__':
#     main()