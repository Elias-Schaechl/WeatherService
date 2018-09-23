import urllib.request
import datetime
from WeatherService.weather.MQTTClient import send_message
from WeatherService.config.ConfigHandler import Config


key = Config.http.auth_key
loc = Config.http.weather_loc
url = Config.http.api_url
tp = Config.http.weather_type


def get_weather(type=tp ):
    path = url + "2.5/" + type + "?" + loc + "&appid=" + key
    #time = datetime.datetime
    print("get_weather() ran!")
    print(path)
    contents = urllib.request.urlopen(path).read()
    send_message("/weather", contents)



