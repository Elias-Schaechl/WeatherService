class Config:
    config_directory = 'config.txt'
    def __init__(self):

        pass
    print("ttttt")
    #json_data = open(config_directory).read()
    #print(json_data)
    class mqtt:
        broker_port = 1883
        broker_uri = "vm61.htl-leonding.ac.at"
        test_topic = ""


    class http:
        auth_key = "5cb2b2fa61fa541e7b13255fc29d5c61"
        weather_loc = "q=Leonding,AT"
        api_url = "https://api.openweathermap.org/data/"
        weather_type = "weather"




