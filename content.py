# Set Location - London - This will be used to get the forcast and also be used to get roles within the specific location
# get quotes from a CSV file
# get trends
# get junior data engineering roles with a link
# testing
# error handling 


import csv
import random
from urllib import request
import json
import datetime
import os
from dotenv import load_dotenv

def get_quote():
    try:
        with open('quotes.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')
            rows = list(reader)
        
        random_row = random.choice(rows)
        random_quote = f'Author: {random_row[0]}\nQuote: {random_row[1]}'

    except FileNotFoundError as fnfe:
        print('Unable to open quote file')
    
    return random_quote

get_quote()

def get_location():
    pass

def get_weather_forcast(coords={'lat': 51.5072, 'lon': 0.1276}): #Default coordincates for London
    '''
    Retrieve the current weather forecast from OpenWeatherMap.
    '''
    load_dotenv()
    api_key = os.getenv('openWeatherMapKey')
    url = f''

def get_twitter_trends():
    pass

def get_de_roles():
    pass

if __name__ == '__main__':
    print('\nTesting quote generation...')

    quote = get_quote()
    print(f' - Random Quote is - \n"{quote}"')