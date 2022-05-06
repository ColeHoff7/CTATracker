import requests
import json
import os
from datetime import datetime


class Arrivals():
    def __init__(self):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "apikey.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path) as f:
            self.key = json.load(f)['key']

        self.belmontId = '41320'
        self.southportId = '40360'
        self.timeToWalkToBelmont = 11
        self.timeToWalkToSouthport = 6
    
    def getMinsTilArrival(self, arrival):
        return round((datetime.fromisoformat(arrival["arrT"]) - datetime.now()).total_seconds() / 60)
    
    def getArrivalTimes(self):
        southportTimes = []
        belmontTimes = []
        try:
            southportArrivals = json.loads(requests.get(f'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={self.key}&mapid={self.southportId}&outputType=JSON&rt=Brn').text)['ctatt']['eta']
            belmontArrivals = json.loads(requests.get(f'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={self.key}&mapid={self.belmontId}&outputType=JSON&rt=Red').text)['ctatt']['eta']

            for belArrival in belmontArrivals:
                mins = self.getMinsTilArrival(belArrival)
                if mins > self.timeToWalkToBelmont: 
                    if belArrival["destNm"] == '95th/Dan Ryan':
                        belArrival["destNm"] = '95th/DR'
                    belmontTimes.append(f'{belArrival["destNm"]} {mins}min')

            for spArrival in southportArrivals:
                mins = self.getMinsTilArrival(spArrival)
                if mins > self.timeToWalkToSouthport: 
                    southportTimes.append(f'{spArrival["destNm"]} {mins}min')
        except Exception as err:
            print(err)
        finally:
            return [southportTimes, belmontTimes]

