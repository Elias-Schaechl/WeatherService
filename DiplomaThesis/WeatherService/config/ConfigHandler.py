class Config:

    config_directory = 'config.txt'

    def __init__(self):
        pass

    print("ttttt")
    # json_data = open(config_directory).read()
    # print(json_data)

    #mqtt connection
    mqtt_broker_port = 8080
    mqtt_broker_uri = "vm61.htl-leonding.ac.at"
    mqtt_weather_topic = "htlleonding/weather/actual/"

    #http connection
    http_auth_key = "5cb2b2fa61fa541e7b13255fc29d5c61"
    http_weather_loc = "q=Leonding,AT"
    http_api_url = "https://api.openweathermap.org/data/"
    http_weather_type = "weather"

    #json paths

    #mqtt topics
    topic_temp = "temp"
    topic_wind_deg = "wind_deg"
    topic_wind_speed = "wind_speed"
    topic_humidity = "humidity"
    topic_pressure = "pressure"
