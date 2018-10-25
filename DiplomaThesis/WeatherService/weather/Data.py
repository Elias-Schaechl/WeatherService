import json
import time

from config.ConfigHandler import Config


# The basic structure how all
class Data:
    # types = ["wind speed", "wind direction", "temperature"]
    # Initializes an Object
    def __init__(self, value=None, timestamp=None, unit=None, topic=None):
        self.value = value
        self.timestamp = timestamp
        self.unit = unit
        self.topic = topic

    # Generates a Json of an Object
    def Jsonify(self):
        if isinstance(self.value, str):
            return "{\"value\":" + "\"" + str(self.value) + "\"" \
                   + ",\"timestamp\":" + str(int(self.timestamp)) + "\"" \
                   + ",\"unit\":\"" + self.unit + "\"}"
        return "{\"value\":" + str(self.value) \
               + ",\"timestamp\":" + str(int(self.timestamp)) \
               + ",\"unit\":\"" + self.unit + "\"}"


class JsonObject(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

    def __str__(self):
        return json.dumps(self.__dict__)


class Weather:
    temp = Data()
    pressure = Data()
    humidity = Data()
    wind_speed = Data()
    wind_deg = Data()
    weather_status = Data()

    def SetTemp(self, temp):
        temp = temp - 273.15
        if temp == self.temp.value:
            return None
        self.temp = Data(value=temp, timestamp=time.time(), topic=Config.topic_temp
                         , unit=Config.unit_temp)
        return Config.mqtt_weather_topic + self.temp.topic, self.temp.Jsonify()

    def SetPressure(self, pressure):
        if pressure == self.pressure.value:
            return None
        self.pressure = Data(value=pressure, timestamp=time.time(), topic=Config.topic_pressure
                             , unit=Config.unit_pressure)
        return Config.mqtt_weather_topic + self.pressure.topic, self.pressure.Jsonify()

    def SetHumidity(self, humidity):
        if humidity == self.humidity.value:
            return None
        self.humidity = Data(value=humidity, timestamp=time.time(), topic=Config.topic_humidity
                             , unit=Config.unit_humidity)
        return Config.mqtt_weather_topic + self.humidity.topic, self.humidity.Jsonify()

    def SetWindSpeed(self, wind_speed):
        if wind_speed == self.wind_speed.value:
            return None
        self.wind_speed = Data(value=wind_speed, timestamp=time.time(), topic=Config.topic_wind_speed
                               , unit=Config.unit_wind_speed)
        return Config.mqtt_weather_topic + self.wind_speed.topic, self.wind_speed.Jsonify()

    def SetWindDeg(self, wind_deg):
        if wind_deg == self.wind_deg.value:
            return None
        self.wind_deg = Data(value=wind_deg, timestamp=time.time(), topic=Config.topic_wind_deg
                             , unit=Config.unit_wind_deg)
        return Config.mqtt_weather_topic + self.wind_deg.topic, self.wind_deg.Jsonify()

    def SetWeatherStatus(self, weather_status):
        if weather_status == self.weather_status.value:
            return None
        self.weather_status = Data(value=weather_status, timestamp=time.time(), topic=Config.topic_weather_status
                                   , unit=Config.unit_weather_status)
        return Config.mqtt_weather_topic + self.weather_status.topic, self.weather_status.Jsonify()
