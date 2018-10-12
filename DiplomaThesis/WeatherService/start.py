import time
from WeatherService.config.ConfigHandler import Config
from WeatherService.weather.HTTPClient import get_weather, get_forecast


while (True):
    get_weather()
    get_forecast()
    time.sleep(Config.http_request_cycle_duration)
