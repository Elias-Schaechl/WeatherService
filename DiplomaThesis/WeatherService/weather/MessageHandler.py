from WeatherService.weather.Data import Weather
from WeatherService.config.ConfigHandler import Config
from WeatherService.weather.Data import JsonObject
from WeatherService.weather.MQTTClient import send_message
import json

class DataHandler():

    weatherData: Weather

    def handleMqttData(payload, topic, timestamp):
        print(f"{timestamp}___{topic}___{payload}")
        return

    def handleApiData(self, contents):
        # Config.mqtt.

        weather = JsonObject(contents)
        self.weatherData.SetTemp(weather.main['temp'])
        self.weatherData.SetPressure(weather.main['pressure'])
        self.weatherData.SetHumidity(weather.main['humidity'])
        self.weatherData.SetWindSpeed(weather.wind['speed'])
        self.weatherData.SetWindDeg(weather.wind['deg'])



        pass




