import requests

# https://pyformat.info/

r = requests.get('http://api.open-notify.org/astros.json')
peoples = r.json()

print('There are {0} people in space right now:'.format(int(peoples["number"])) + '\r\n')
print('{:20}'.format('Name') + ' | ' + '{:20}'.format('Craft'))
print('{:20}'.format('_'*21) + '|' + '{:20}'.format('_'*21))
for people in peoples["people"]:
    print('{:20}'.format(people["name"]) + ' | ' + '{:20}'.format(people["craft"]))





