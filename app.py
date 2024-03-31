import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()
from flask import Flask, jsonify, render_template
import pandas as pd
from pyspark.sql.functions import sum


app = Flask(__name__)

# Function to convert Spark DataFrame to JSON format
def dataframe_to_json(dataframe):
    pandas_df = dataframe.toPandas()
    return pandas_df.to_dict(orient="records") 

# Route for the landing page
@app.route('/')
def index():
    return render_template('index.html')

# Reading the CSV data into a Spark DataFrame with schema inference and header recognition
covid_df = spark.read.option("header",True).option("inferSchema", True).csv("covidCases.csv")

# Calculating and sorting data for various metrics
most_affected=covid_df.withColumn("DeathRate", covid_df["Deaths"]/covid_df["NoOfCases"]).orderBy("DeathRate", ascending=False).select("Country","DeathRate").limit(1)
least_affected=covid_df.withColumn("DeathRate", covid_df["Deaths"]/covid_df["NoOfCases"]).orderBy("DeathRate", ascending=True).select("Country","DeathRate").limit(1)
highest_covid_case = covid_df.orderBy("NoOfCases", ascending=False).select("Country", "NoOfCases").limit(1)
minimum_covid_case = covid_df.orderBy("NoOfCases", ascending=True).select("Country", "NoOfCases").limit(1)
total_cases = covid_df.agg(sum("NoOfCases").alias("Total Cases"))
most_efficient = covid_df.select("Country", (covid_df.Recovery/covid_df.NoOfCases).alias("RecoveryRate")).orderBy("RecoveryRate", ascending=False).limit(1)
least_efficient = covid_df.select("Country", (covid_df.Recovery/covid_df.NoOfCases).alias("RecoveryRate")).orderBy("RecoveryRate", ascending=True).limit(1)
least_suffering = covid_df.select("Country").orderBy("CriticalCases", ascending=True).limit(1)
still_suffering = covid_df.select("Country").orderBy("CriticalCases", ascending=False).limit(1)

# Endpoints to serve the JSON data of calculated metrics
@app.route('/show_covid_data', methods=['GET'])
def show_covid_data():
    return dataframe_to_json(covid_df)

@app.route('/most_affected_country', methods=['GET'])
def get_most_affected_country():
    return dataframe_to_json(most_affected)

@app.route('/least_affected_country', methods=['GET'])
def get_least_affected_country():
    return dataframe_to_json(least_affected)

@app.route('/highest_covid_case_country', methods=['GET'])
def get_highest__covid_case_country():
    return dataframe_to_json(highest_covid_case)

@app.route('/minimum_covid_case_country', methods=['GET'])
def get_minimum_covid_case_country():
    return dataframe_to_json(minimum_covid_case)

@app.route('/total_cases_globally', methods=['GET'])
def get_total_cases_globally():
    return dataframe_to_json(total_cases)

@app.route('/most_efficient_country', methods=['GET'])
def get_most_efficient_country ():
    return dataframe_to_json(most_efficient)

@app.route('/least_efficient_country', methods=['GET'])
def get_least_efficient_country ():
    return dataframe_to_json(least_efficient)

@app.route('/still_suffering_country', methods=['GET'])
def get_still_suffering_country():
    return dataframe_to_json(still_suffering)

@app.route('/least_suffering_country', methods=['GET'])
def get_least_suffering_country():
    return dataframe_to_json(least_suffering)

# For plotting graphs
@app.route('/data')
def data():
    data = dataframe_to_json(covid_df)
    return (data)

if __name__ == '__main__':
    app.run(debug=True)
