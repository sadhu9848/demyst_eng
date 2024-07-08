from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import random

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Anonymize Data") \
    .getOrCreate()

# Define UDFs for anonymization
def anonymize_name(name):
    return f'FirstName{random.randint(100000, 999999)}'

def anonymize_address(address):
    return f'Address{random.randint(100000, 999999)}'

# Register UDFs with Spark
anonymize_name_udf = udf(anonymize_name, StringType())
anonymize_address_udf = udf(anonymize_address, StringType())

# Load CSV file into Spark DataFrame
df = spark.read.csv('people.csv', header=True, inferSchema=True)

# Apply anonymization UDFs to relevant columns
df_anonymized = df.withColumn('first_name', anonymize_name_udf('first_name')) \
                  .withColumn('last_name', anonymize_name_udf('last_name')) \
                  .withColumn('address', anonymize_address_udf('address'))

# Write anonymized DataFrame back to CSV
df_anonymized.write.csv('anonymized_people.csv', header=True, mode='overwrite')

# Stop Spark session
spark.stop()
