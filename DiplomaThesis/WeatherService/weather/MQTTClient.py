import datetime
import threading
import paho.mqtt.client as mqtt

from config.ConfigHandler import Config



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("on_connect ran with result code: " + str(rc))
    make_subscriptions()


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("on_message ran!")
    timestamp = datetime.datetime.now()
    # DataHandler.handleMqttData(msg.payload, msg.topic, timestamp)
    print("MQTT-Recieved: " + msg.topic + " " + str(msg.payload))
    # print(timestamp)


def make_subscriptions():
    client.subscribe("htllending/#")


def send_message(topic, payload):

    qos = 1
    retain = True
    print(topic + ": " + payload)
    client.publish(topic, payload, qos, retain)
    return


def start_client():
    print("start_client ran!")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(brokerURI, brokerPort, 60)
    client.loop_forever()



def test_thread():
    while True:
        i = input()
        if i == "":
            break
        print(i)


brokerURI = Config.mqtt_broker_uri
brokerPort = Config.mqtt_broker_port
testTopic = Config.mqtt_weather_topic

client = mqtt.Client()
client.username_pw_set(Config.mqtt_client_username, Config.mqtt_client_password)

clientThread = threading.Thread(name='MqttClientThread',target=start_client)

clientThread.start()

print("M1ttClient end")
