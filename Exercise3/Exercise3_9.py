# File name:    Exercise3_9.py
# Author:       Eerik Vainio
# Description:  User can create a weather station and add weather observations.
#               User can query for the latest observation, and number of total
#               observations.

class WeatherStation:
    def __init__(self, name: str):
        self.name = name
        self.list_of_observations = []

    def __str__(self):
        return f'{self.name}, {len(self.list_of_observations)} observations'

    def add_observation(self, observation: str):
        self.list_of_observations.append(observation)
    
    def latest_observation(self):
        if (len(self.list_of_observations) > 0):
            return self.list_of_observations[-1]
        else:
            return ""
        
    def number_of_observations(self):
        return len(self.list_of_observations)
    
station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())
station.add_observation("Thunderstorm")
print(station.latest_observation())
print(station.number_of_observations())
print(station)

