import requests
import csv
import logging


def fetch_country_data(country_name):
    url = f'https://disease.sh/v3/covid-19/countries/{country_name}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch COVID-19 data for {country_name}. Status code:", response.status_code)
        return None
    

def extract_data():
    logging.info("Starting data extraction")   
    data = 'covidCases.csv'
    countries = ["China", "India", "USA" ,"Angola" ,"Russia", "Ukraine", "France", "Germany", "Greece", "Italy", "Nepal",
                "Kenya", "Australia", "Spain", "Canada", "Georgia", "Japan", "Chile",
                "Pakistan", "Turkey"]

    # Open CSV file for writing
    with open(data, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(['Country', 'TotalTests', 'NoOfCases', 'Recovery', 'Deaths', 'ActiveCases', 'CriticalCases'])

        # Iterate over countries and fetch data
        for country in countries:
            country_data = fetch_country_data(country)
            if country_data:
                writer.writerow([country_data['country'], country_data['tests'], country_data['cases'],
                                country_data['recovered'],country_data['deaths'], country_data['active'], country_data['critical']])
    print("Successfully Fetched!")
    logging.info("Data extraction completed")

extract_data()