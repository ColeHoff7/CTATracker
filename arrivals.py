import requests
import json 
from datetime import datetime


class Arrivals():
    def __init__(self):
        with open('apikey.json') as f:
            self.key = json.load(f)['key']

        self.belmontId = '41320'
        self.southportId = '40360'
        self.timeToWalkToBelmont = 11
        self.timeToWalkToSouthport = 6
    
    def getMinsTilArrival(self, arrival):
        return round((datetime.fromisoformat(arrival["arrT"]) - datetime.now()).total_seconds() / 60)
    
    def getArrivalTimes(self):
        southportArrivals = json.loads(requests.get(f'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={self.key}&mapid={self.southportId}&outputType=JSON&rt=Brn').text)['ctatt']['eta']
        belmontArrivals = json.loads(requests.get(f'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={self.key}&mapid={self.belmontId}&outputType=JSON&rt=Red').text)['ctatt']['eta']
        southportTimes = []
        belmontTimes = []

        for belArrival in belmontArrivals:
            mins = self.getMinsTilArrival(belArrival)
            if mins > self.timeToWalkToBelmont: 
                belmontTimes.append(f'{belArrival["destNm"]} {mins}min')

        for spArrival in southportArrivals:
            mins = self.getMinsTilArrival(spArrival)
            if mins > self.timeToWalkToSouthport: 
                southportTimes.append(f'{spArrival["destNm"]} {mins}min')

        return [southportTimes, belmontTimes]
