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

def get_location():
    pass

def get_weather_forcast(coords={'lat': 51.5266694, 'lon': 0.0798926}): #Default coordincates for London
    '''
    Retrieve the current weather forecast from OpenWeatherMap.
    '''
    try:
        load_dotenv()
        api_key = os.getenv('openWeatherMapKey')
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units=metric'
        data = json.load(request.urlopen(url))

        forecast = {
            'city': data['city']['name'],
            'country': data['city']['country'],
            'period': list()}
        
        for period in data['list'][0:9]:
            forecast['period'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                       'temp': round(period['main']['temp']),
                                       'description': period['weather'][0]['description'].title(),
                                       'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'})
            
        return forecast

    except Exception as e:
        print(e)

def get_twitter_trends():
    pass

def get_de_roles():
    pass

if __name__ == '__main__':
    # print('\nTesting quote generation...')

    # quote = get_quote()
    # print(f' - Random Quote is - \n"{quote}"')

    print('\n - Testing wather forecast retrieval...')

    forecast = get_weather_forcast()
    if forecast:
        print(f'\nWeather forcase for {forecast["city"]}, {forecast["country"]} is...')
        for period in forecast['period']:
            print(f' - {period["timestamp"]} | {period["temp"]}c | {period["description"]}')