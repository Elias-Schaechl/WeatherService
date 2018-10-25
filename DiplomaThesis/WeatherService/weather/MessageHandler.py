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

        temp = self.weatherData.SetTemp(weather.main['temp'])
        if temp is not None:
            send_message(temp[0], temp[1])

        pressure = self.weatherData.SetPressure(weather.main['pressure'])
        if pressure is not None:
            send_message(pressure[0], pressure[1])

        humidity = self.weatherData.SetHumidity(weather.main['humidity'])
        if humidity is not None:
            send_message(humidity[0], humidity[1])

        windsp = weather.wind['speed']
        wind_speed = self.weatherData.SetWindSpeed(windsp)
        if wind_speed is not None:
            send_message(wind_speed[0], wind_speed[1])
        if windsp > 1:
            wind_deg = self.weatherData.SetWindDeg(weather.wind['deg'])
            if wind_deg is not None:
                send_message(wind_deg[0], wind_deg[1])

        weather_status = self.weatherData.SetWeatherStatus(weather.weather[0]['id'])
        if weather_status is not None: send_message(weather_status[0], weather_status[1])

        pass

    def handleApiForecast(self, contents):
        forecast = JsonObject(contents)
        #print(forecast)
        del forecast.__dict__["city"]
        del forecast.__dict__["cod"]
        del forecast.__dict__["message"]
        forecast.__dict__["city"] = "Leonding"
        for i  in range(0,forecast.__dict__["cnt"]):
            #print(forecast.__dict__["list"][i])
            for k, v in forecast.__dict__["list"][i]["main"].items():
                #print(k + str(v))
                if k == "temp" or k == "temp_min" or k == "temp_max":
                    forecast.__dict__["list"][i]["main"][k] = round(forecast.__dict__["list"][i]["main"][k] - 273.1, 2)


        print(forecast)
        send_message(Config.mqtt_forecast_topic, str(forecast))

        pass
