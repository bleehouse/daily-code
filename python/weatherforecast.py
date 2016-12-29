import requests


def sort_list(keyname, oldlist):
    newlist = sorted(oldlist, key=lambda k: k[keyname])
    return newlist


def degrees_to_cardinal(d):
    '''
    note: this is highly approximate...
    '''
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    ix = int((d + 11.25)/22.5)
    return dirs[ix % 16]

unitsname = 'Celsius'
city = str(input('Where are you? ')).lower()
units = str(input("Choose temperature units([1] Celsius(Default), [2] Fahrenheit): ")).lower()


if units is None or units == "" or units == 'celsius':
    units = 'metric'
    unitsname = 'Celsius'
elif units == 'fahrenheit':
    units = 'imperial'
    unitsname = 'Fahrenheit'
else:
    units = 'metric'
    unitsname = 'Celsius'

# Metric: Celsius, Imperial: Fahrenheit.
payload = {'q': city.lower(), 'APPID': 'c1835f97d8bb1db2b413d9e910d83866', 'units': units} 

r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)

forecast = r.json()

print('City : {0}, Weather : {1} , Temperature : {2} {3}, Wind : {4} '.format(
        city,
        forecast['weather'][0]['main'],
        forecast['main']['temp'],
        unitsname,
        degrees_to_cardinal(int(forecast['wind']['deg']))
    ))

# http://docs.python-requests.org/en/master/
# https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f