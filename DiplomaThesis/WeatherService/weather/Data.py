import json
from WeatherService.weather.MQTTClient import send_message
import time

#The basic structure how all
class Data:
    #types = ["wind speed", "wind direction", "temperature"]
    #Initializes an Object
    def __init__(self, value, timestamp, topic=None):
        self.value = value
        self.timestamp = timestamp
        self.topic = topic


    #Generates a Json of an Object
    def Jsonify(self):
        return "{\"unit\":\"" + self.unit + "\",\"value\":" + self.value + ",\"timestamp\":\"" + self.timestamp + "\"}"

class JsonObject(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


class Weather:
    temp: Data
    pressure: Data
    humidity: Data
    wind_speed: Data
    wind_deg: Data

    def SetTemp(self, temp):
        if temp == self.temp: pass
        self.temp = Data(temp, time.time(), "test/temp")
        send_message(self.temp.Jsonify())


    def SetPressure(self, pressure):
        pass

    def SetHumidity(self, humidity):
        pass

    def SetWindSpeed(self, wind_speed):
        pass

    def SetWindDeg(self, wind_deg):
        pass


class WeatherSchool(Weather):
    title = "School"

class WeatherExtern(Weather):
    title = "External"

