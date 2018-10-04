import json
from WeatherService.weather.MQTTClient import send_message
import time


# The basic structure how all
class Data:
    # types = ["wind speed", "wind direction", "temperature"]
    # Initializes an Object
    def __init__(self, value=None, timestamp=None, topic=None):
        self.value = value
        self.timestamp = timestamp
        self.topic = topic

    # Generates a Json of an Object
    def Jsonify(self):
        return "{\"value\":" + str(self.value) + ",\"timestamp\":\"" + str(self.timestamp) + "\"}"


class JsonObject(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


class Weather:
    temp = Data()
    pressure = Data()
    humidity = Data()
    wind_speed = Data()
    wind_deg = Data()

    def SetTemp(self, temp):
        if temp == self.temp.value: return
        self.temp = Data(temp, time.time(), "test/temp")
        send_message(self.temp.topic, self.temp.Jsonify())

    def SetPressure(self, pressure):
        if pressure == self.pressure.value: return
        self.pressure = Data(pressure, time.time(), "test/pressure")
        send_message(self.pressure.topic, self.pressure.Jsonify())

    def SetHumidity(self, humidity):
        if humidity == self.humidity.value: return
        self.humidity = Data(humidity, time.time(), "test/humidity")
        send_message(self.humidity.topic, self.humidity.Jsonify())

    def SetWindSpeed(self, wind_speed):
        if wind_speed == self.wind_speed.value: return
        self.wind_speed = Data(wind_speed, time.time(), "test/wind_speed")
        send_message(self.wind_speed.topic, self.wind_speed.Jsonify())

    def SetWindDeg(self, wind_deg):
        if wind_deg == self.wind_deg.value: return
        self.wind_deg = Data(wind_deg, time.time(), "test/wind_deg")
        send_message(self.wind_deg.topic, self.wind_deg.Jsonify())


