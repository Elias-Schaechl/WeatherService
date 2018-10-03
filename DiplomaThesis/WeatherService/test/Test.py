import unittest

from WeatherService.weather.MQTTClient import send_message
from WeatherService.weather.Data import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_mqttClient(self):
        send_message("/","lululu")

    def test_minor(self):
        test = Data("C", "4", "1.1")
        print(test.Jsonify())

        a = Data("C", "10", "1")
        b = Data("C", "20", "1")

        school = WeatherSchool
        extern = WeatherExtern
        test1 = Weather
        test2 = Weather

        school.temperature = a
        extern.temperature = b

        test1.temperature = a
        test2.temperature = b

        print(school.temperature.Jsonify())
        print(extern.temperature.Jsonify())
        print(test1.temperature.Jsonify())
        print(test2.temperature.Jsonify())
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()


