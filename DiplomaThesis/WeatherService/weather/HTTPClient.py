import urllib.request
import datetime

from WeatherService.config.ConfigHandler import Config
from WeatherService.weather.MessageHandler import DataHandler

key = Config.http_auth_key
loc = Config.http_weather_loc
url = Config.http_api_url
tp = Config.http_weather_type

dH = DataHandler()


def get_weather(type=tp):
    path = url + "2.5/" + type + "?" + loc + "&appid=" + key
    # time = datetime.datetime
    print("get_weather() ran!")
    print(path)
    contents = urllib.request.urlopen(path).read()
    dH.handleApiData(contents)
