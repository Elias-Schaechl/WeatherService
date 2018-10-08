from WeatherService.weather.HTTPClient import get_weather
import time
#type = "forecast"
type = "weather"

while (True):
    get_weather(type)
    time.sleep(60)