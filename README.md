# Covid-19_Data_Dashboard
<h3>Python Spark Rest API Combined Assignment</h3>
<br>
Task 1 and Task 2 is performed in Queries.ipynb file.
<br> 
Task 3 is perfomed in app.py file and it's html part is located in templates folder.
<br>
<br>
This Python-based web application leverages Flask and PySpark to serve a dynamic COVID-19 data dashboard. It presents up-to-date information on the COVID-19 pandemic across 20 countries, with a focus on various metrics like active cases, deaths, total cases, recoveries, critical cases, and total tests conducted. Users can interact with the dashboard to view specific data visualizations based on different parameters.
<br>

![alt text](https://github.com/Sonam-25/Covid-19_Data_Dashboard/blob/main/Home_page.png)

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

![alt text](https://github.com/Sonam-25/Covid-19_Data_Dashboard/blob/main/subquery_fetching_json_data.png)
