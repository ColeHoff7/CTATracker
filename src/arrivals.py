import requests
import json
import os
from datetime import datetime

class Arrivals():
    def __init__(self):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        abs_file_path = os.path.join(script_dir, "apikey.json")
        with open(abs_file_path) as f:
            self.key = json.load(f)['key']

        config_file_path = os.path.join(script_dir, "../config.json")
        with open(config_file_path) as f:
            self.stations = json.load(f)['stations']
    
    def getMinsTilArrival(self, arrival):
        return round((datetime.fromisoformat(arrival["arrT"]) - datetime.now()).total_seconds() / 60)
    
    def getArrivalTimes(self, station):
        """
        Given a station (structure defined in config.json), fetch the arrivals and structure them into a string. Returns the array of strings of upcoming arrivals
        """
        arrival_times = []
        try:
            arrivals = json.loads(requests.get(f'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={self.key}&mapid={station['id']}&outputType=JSON&rt={station['line']}').text)['ctatt']['eta']))
            for arrival in arrivals:
                mins = self.getMinsTilArrival(arrival)
                # eliminate the arrival if we can't feasibly walk there in time
                if mins > station['cutoffTime']:
                    arrival_times.append(f'{arrival["destNm"][:8]} {mins}min')
        except Exception as err:
            print(err)
        finally:
            return arrival_times