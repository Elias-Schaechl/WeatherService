import json

from .Data import Weather, JsonObject
from .MQTTClient import send_message
from config.ConfigHandler import Config


class DataHandler():
    weatherData = Weather()

    def handleMqttData(payload, topic, timestamp):
        print(f"{timestamp}___{topic}___{payload}")
        return

    def handleApiData(self, contents):
        # Config.mqtt.

        weather = JsonObject(contents)
        self.weatherData.SetTemp(weather.main['temp'])
        self.weatherData.SetPressure(weather.main['pressure'])
        self.weatherData.SetHumidity(weather.main['humidity'])
        wind_speed = weather.wind['speed']
        self.weatherData.SetWindSpeed(wind_speed)
        if wind_speed > 1:
            self.weatherData.SetWindDeg(weather.wind['deg'])
        self.weatherData.SetWeatherStatus(weather.weather[0]['main'])

        pass

    def handleApiForecast(self, contents):
        forecast = JsonObject(contents)
        print(forecast)
        del forecast.__dict__["city"]
        del forecast.__dict__["cod"]
        del forecast.__dict__["message"]
        forecast.__dict__["city"] = "Leonding"
        print(forecast)
        send_message(Config.mqtt_forecast_topic, str(forecast))

        pass
