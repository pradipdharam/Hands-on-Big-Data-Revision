 # Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate()

# Read CSV file into table
df = spark.read.option("header",True) \
          .csv("data/emp.csv")

df.createOrReplaceTempView("emp")
df1 = spark.sql("select EMPLOYEE_ID as eid, format_number(float(max(SALARY)),2) as max_salary, format_number(avg(SALARY),2) as avg_salary from emp group by EMPLOYEE_ID")
df1.show()


# # Create temporary table
# spark.read.option("header",True) \
#           .csv("/Users/admin/simple-zipcodes.csv") \
#           .createOrReplaceTempView("Zipcodes")