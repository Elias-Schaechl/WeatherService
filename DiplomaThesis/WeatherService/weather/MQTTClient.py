import datetime

import paho.mqtt.client as mqtt
from WeatherService.config.ConfigHandler import Config
from WeatherService.weather.MessageHandler import *
import threading



def on_connect(client, userdata, flags, rc):
    print("on_connect ran with result code: " + str(rc))
    make_subscriptions()

def on_message(client, userdata, msg):
    print("on_message ran!")
    timestamp = datetime.datetime.now()
    handleData(msg.payload, msg.topic, timestamp)
    #print("MQTT-Recieved: " + msg.topic + " " + str(msg.payload))
    #print(timestamp)

def make_subscriptions():
    client.subscribe("/test/#")

def send_message(topic, payload):
    qos = 1
    retain = False
    client.publish(topic, payload, qos, retain)
    return


def start_client():

    client.loop_forever()

def test_thread():
    while True:
        i = input()
        if i == "":
            break
        print(i)


brokerURI = Config.mqtt.broker_uri
brokerPort = Config.mqtt.broker_port
testTopic = Config.mqtt.test_topic

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(brokerURI, brokerPort, 60)

testThread = threading.Thread(target=test_thread)
clientThread = threading.Thread(target=start_client)

testThread.start()
clientThread.start()








