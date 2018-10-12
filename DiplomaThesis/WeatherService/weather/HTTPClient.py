import urllib.request
import datetime

from WeatherService.config.ConfigHandler import Config
from WeatherService.weather.MessageHandler import DataHandler

key = Config.http_auth_key
loc = Config.http_weather_loc
url = Config.http_api_url
tp_weather = Config.http_weather_type
tp_forecast = Config.http_forecast_type


dH = DataHandler()


def get_weather():
    path = url + "2.5/" + tp_weather + "?" + loc + "&appid=" + key
    print("get_weather() ran!")
    print(path)
    contents = urllib.request.urlopen(path).read()
    dH.handleApiData(contents)

def get_forecast():
    path = url + "2.5/" + tp_forecast + "?" + loc + "&appid=" + key
    print("get_forecast() ran!")
    print(path)
    contents = urllib.request.urlopen(path).read()
    dH.handleApiForecast(contents)