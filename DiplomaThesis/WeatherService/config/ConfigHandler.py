class Config:
    config_directory = 'config.txt'

    def __init__(self):
        pass

    print("Config ran!")
    # json_data = open(config_directory).read()
    # print(json_data)

    # mqtt connection
    mqtt_broker_port = 8080
    mqtt_broker_uri = "vm61.htl-leonding.ac.at"
    mqtt_weather_topic = "htlleonding/outdoor/weather/actual"
    mqtt_forecast_topic = "htlleonding/outdoor/weather/forecast"
    mqtt_client_username = "weather_client"
    mqtt_client_password = "dhtnd54t"

    # http connection
    http_auth_key = "5cb2b2fa61fa541e7b13255fc29d5c61"
    http_weather_loc = "q=Leonding,AT"
    http_api_url = "https://api.openweathermap.org/data/"
    http_weather_type = "weather"
    http_forecast_type = "forecast"
    http_request_cycle_duration_weather = 60     # In seconds, 1 m
    http_request_cycle_duration_forecast = 10800     # In seconds, 5 h

    # json paths

    # mqtt topics
    topic_temp = "/temp"
    topic_wind_deg = "/wind_deg"
    topic_wind_speed = "/wind_speed"
    topic_humidity = "/humidity"
    topic_pressure = "/pressure"
    topic_weather_status = "/status"
