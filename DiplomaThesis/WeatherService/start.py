import time
import threading

from config.ConfigHandler import Config
from weather.HTTPClient import get_weather, get_forecast

def start_weather_loop():
    while (True):
        get_weather()
        time.sleep(Config.http_request_cycle_duration_weather)

def start_forecast_loop():
    pass
    while (True):
        get_forecast()
        time.sleep(Config.http_request_cycle_duration_forecast)


last_time_forecast = time.ctime(0)
forecast_frequency = 1000

forecast_thread = threading.Thread(name="ForecastLoop",target=start_forecast_loop)
weatherThread = threading.Thread(name="WeatherLoop", target=start_weather_loop)

forecast_thread.start()
weatherThread.start()

print("reached end of start")




