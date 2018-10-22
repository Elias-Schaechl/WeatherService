import urllib.request
import datetime

from config.ConfigHandler import Config
from .MessageHandler import DataHandler

key = Config.http_auth_key
loc = Config.http_weather_loc
url = Config.http_api_url
tp_weather = Config.http_weather_type
tp_forecast = Config.http_forecast_type


dH = DataHandler()


def get_weather():
    path = url + "2.5/" + tp_weather + "?" + loc + "&appid=" + key
    print(path)
    contents = urllib.request.urlopen(path).read()
    dH.handleApiData(contents)
    print("get_weather() ran!")
    #try:
    #    contents = urllib.request.urlopen(path).read()
    #    dH.handleApiData(contents)
    #except:
    #    print("get_weather() ran with errors!")
    #else:
    #    print("get_weather() ran!")


def get_forecast():
    path = url + "2.5/" + tp_forecast + "?" + loc + "&appid=" + key
    print(path)
    contents = urllib.request.urlopen(path).read()
    dH.handleApiForecast(contents)
    #try:
    #    contents = urllib.request.urlopen(path).read()
    #    dH.handleApiForecast(contents)
    #except:
    #    print("get_forecast ran with errors!")
    #else:
    #    print("get_forecast() ran!")
