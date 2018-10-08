import time
from WeatherService.config.ConfigHandler import Config
from WeatherService.weather.HTTPClient import get_weather

# type = "forecast"
type = "weather"

while (True):
    get_weather(type)
    time.sleep(Config.http_request_cycle_duration)
