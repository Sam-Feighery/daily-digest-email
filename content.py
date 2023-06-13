# Set Location - London - This will be used to get the forecast and also be used to get roles within the specific location
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

def get_weather_forecast(coords={'lat': 51.5323935 , 'lon': -0.086078}): #Default coordincates for London
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

    # print('\n - Testing weather forecast retrieval...')

    # forecast = get_weather_forecast()
    # if forecast:
    #     print(f'\nWeather forecast for {forecast["city"]}, {forecast["country"]} is...')
    #     for period in forecast['period']:
    #         print(f' - {period["timestamp"]} | {period["temp"]}c | {period["description"]}')
    
    # hither_green = {'lat': 51.4515872,'lon': -0.0006473} # coordinates for Texas State Capitol
    # forecast = get_weather_forecast(coords = hither_green) # get Austin, TX forecast
    # if forecast:
    #     print(f'\nWeather forecast for {forecast["city"]}, {forecast["country"]} is...')
    #     for period in forecast['period']:
    #         print(f' - {period["timestamp"]} | {period["temp"]}°C | {period["description"]}')

    # invalid = {'lat': 1234.5678 ,'lon': 1234.5678} # invalid coordinates
    # forecast = get_weather_forecast(coords = invalid) # get forecast for invalid location
    # if forecast is None:
    #     print('Weather forecast for invalid coordinates returned None')
    pass