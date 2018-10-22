import time
from config.ConfigHandler import Config
from weather.HTTPClient import get_weather, get_forecast


while (True):
    get_weather()
    get_forecast()
    time.sleep(Config.http_request_cycle_duration)
