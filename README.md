# Covid-19_Data_Dashboard
<h3>Python Spark Rest API Combined Assignment</h3>
<br>
main.py is the entry point to the entire application, responsible for executing extract.py and app.py
<br>
Task 1 is src>>extract.py file which extracts the COVID-19 data from provided API to write and save in a csv file (covidCases.csv).
<br> 
Task 2 is performed in Queries.ipynb which processes all the queries over the dataframe.
<br>
Task 3 is perfomed in src>>app.py file and it's rendered html page is located in src>>templates folder.
<br>
config.yaml is aconfiguration that allows us to easily adjust settings without modifying the codebase.
<br>
requirements.txt involves listing all the Python packages on which our application depends on.
<br>
This Python-based web application leverages Flask and PySpark to serve a dynamic COVID-19 data dashboard. It presents up-to-date information on the COVID-19 pandemic across 20 countries, with a focus on various metrics like active cases, deaths, total cases, recoveries, critical cases, and total tests conducted. Users can interact with the dashboard to view specific data visualizations based on different parameters.
<br>

![image](https://github.com/Sonam-25/Covid-19_Data_Dashboard/assets/157121507/ac9d0d90-f798-4327-8919-fca98b95de4e)

<h2>How It Works</h2>
<br>
<ins>Data Processing</ins>: The application reads COVID-19 case data from a CSV file into a Spark DataFrame. It then calculates various metrics, such as the death rate, recovery rate, and number of critical cases, among others.
<br>
<ins>Web Server</ins>: Flask serves as the backend, exposing several endpoints that return JSON-formatted data for the front end to consume.
<br>
<ins>Front End Visualization</ins>: The front end utilizes Chart.js to fetch the JSON data from the Flask server and render interactive bar charts based on the selected parameter (e.g., Deaths, Recovery, Total Cases).
<hr>
Each menu option fetches the data in the json format based on their respective subquery.
<br>

![image](https://github.com/Sonam-25/Covid-19_Data_Dashboard/assets/157121507/0b1bee15-9e42-49d8-bcf8-b61b1b8e8ef2)

