from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import os
import re

MAX_MEMORY = "64g"
data_dir = 'mimic-iii-clinical-database-1.4'
output_dir ='data'

if __name__ == "__main__":
# reads all the csvs and writes them to parquet files
    spark = SparkSession.builder \
        .appName("csv_to_parquet") \
        .config("spark.executor.memory", MAX_MEMORY) \
        .config("spark.driver.memory", MAX_MEMORY) \
        .getOrCreate()

    files = os.listdir(data_dir)
    for file in files:
        if re.search('[.]csv', file):
            print('reading {} ...'.format(file))
            path = data_dir + '/' + file
            df = spark.read.format('csv') \
                .option('header',True) \
                .option('multiLine', True) \
                .option('quote','"') \
                .option('escape','"') \
                .option('inferSchema', True)\
                .load(path)
            for c in df.columns:
                if re.search('.*DATE$', c):
                    df = df.withColumn(c, col(c).cast(DateType()))
                if re.search('.*TIME$', c):
                    df = df.withColumn(c, col(c).cast(TimestampType()))
                if re.search('.*ID$', c):
                    df = df.withColumn(c, col(c).cast(IntegerType()))
            df.show(4)
            dest = output_dir +'/'+ file[:-4] + '.parquet'
            print('schema {}'.format(df.schema))
            print('writting {} ... '.format(dest))
            df.write.mode('overwrite').parquet(dest)
    spark.stop()
    print('completed')
