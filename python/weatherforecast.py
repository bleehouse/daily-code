import requests


def sort_list(keyname, oldlist):
    newlist = sorted(oldlist, key=lambda k: k[keyname])
    return newlist

city = str(input('Where are you? '))

payload = {'q': city.lower(), 'APPID': 'c1835f97d8bb1db2b413d9e910d83866', 'units': 'metric'}

r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)

forecast = r.json()

print('{0} weather : {1} degrees Celsius '.format(city, forecast['main']['temp']))

# print(forecast['main']['temp'])

# print(forecast)
# print(forecast['weather'][0]['main'])

# print('There are {0} people in space right now:'.format(int(peoples["number"])) + '\r\n')
# print('{:20}'.format('Name') + ' | ' + '{:20}'.format('Craft'))
# print('{:20}'.format('_'*21) + '|' + '{:20}'.format('_'*21))  

# for people in sort_list("name", peoples["people"]):
#     print('{:20}'.format(people["name"]) + ' | ' + '{:20}'.format(people["craft"]))

# http://docs.python-requests.org/en/master/