apitip = '''
City name, state code and country code divided by comma, Please, refer to ISO 3166 for
the state codes or country codes.
You can specify the parameter not only in English. In this case,
the API response should be returned in the same language as the language of requested
location name if the location is in our predefined list of more than 200,000 locations
api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={API key}'''

from weathermethod import tomydict


class Getweather:
    key = '735f9ff24a1deda1bb98344607af33c8'

    def __init__(self, cityname='Enugu', statecode=''):
        self.cityname = cityname
        self.statecode = statecode
        self.weather = f"http://api.openweathermap.org/data/2.5/weather?q={self.cityname},{self.statecode}&appid={self.key}"
        self.weather1 = f"http://api.openweathermap.org/data/2.5/weather?q={self.cityname}&appid={self.key}"

    def make_request(self):
        import requests
        self.response = requests.get(self.weather)
        self.data = self.response.text
        print(self.data)

    def harvestingdata(self):
        import json
        self.data = json.loads(self.data)

    def harvesteddata(self):
        coordinates = self.data['coord']
        weather = (tomydict(self.data['weather']))
        main = self.data['main']
        base = (self.data['base'])
        visibility = (self.data['visibility'])
        wind = (self.data['wind'])
        timezone = (self.data["timezone"])
        clouds = (self.data['clouds'])
        my_dict = {'coordinates': coordinates, 'main': main, 'weather': weather, 'base': base, 'visibility': visibility,
                   'wind': wind, 'timezone': timezone, 'clouds': clouds}
        return my_dict


def runWeather(fcityname='Enugu', fstatecode=''):
    try:
        weatherapi = Getweather(cityname=fcityname, statecode=fstatecode)
        weatherapi.make_request()
        weatherapi.harvestingdata()
        weatherapi.harvesteddata()
    except Exception as err:
        return ('there was an error', err)
    return weatherapi.harvesteddata()
