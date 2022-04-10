import requests
import json 
from datetime import datetime

with open('apikey.json') as f:
    key = json.load(f)['key']

belmontId = '41320'
southportId = '40360'
belmontArrivals = json.loads(requests.get(f'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid={belmontId}&outputType=JSON&rt=Red').text)['ctatt']['eta']
southportArrivals = json.loads(requests.get(f'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid={southportId}&outputType=JSON&rt=Brn').text)['ctatt']['eta']
timeToWalkToBelmont = 11
timeToWalkToSouthport = 6

def getMinsTilArrival(arrival):
    return round((datetime.fromisoformat(arrival["arrT"]) - datetime.now()).total_seconds() / 60)

print('Belmont Arrivals:')
for belArrival in belmontArrivals:
    mins = getMinsTilArrival(belArrival)
    if mins > timeToWalkToBelmont: 
        print(f'{belArrival["destNm"]}: {mins} min')

print()

print('Southport Arrivals:')
for spArrival in southportArrivals:
    mins = getMinsTilArrival(spArrival)
    if mins > timeToWalkToSouthport: 
        print(f'{spArrival["destNm"]}: {mins} min')
