#The basic structure how all
class Data:
    #types = ["wind speed", "wind direction", "temperature"]
    #Initializes an Object
    def __init__(self, unit, value, timestamp, topic=None):
        self.unit = unit
        self.value = value
        self.timestamp = timestamp
        self.topic = topic


    #Generates a Json of an Object
    def Jsonify(self):
        return "{\"unit\":\"" + self.unit + "\",\"value\":" + self.value + ",\"timestamp\":\"" + self.timestamp + "\"}"


class Weather:
    windSpeed: Data
    windDirection: Data
    temperature: Data
    rain: Data

    def __init__(self, unit, value, timestamp):
        self.unit = unit
        self.value = value
        self.timestamp = timestamp

class WeatherShcool(Weather):
    title = "School"

class WeatherExtern(Weather):
    title = "External"

