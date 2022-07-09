import requests
import json


class Weather:
    def __init__(self):
        self.site = 'https://openweathermap.org/'
        self.key = '7f1bc264fc333365d5d6d31a61954955'

    def __get_weather(self, coords):
        req_3 = f'https://api.openweathermap.org/data/2.5/weather?lat={coords[0]}&lon={coords[1]}&appid={self.key}'
        r_3 = requests.get(req_3)
        data = json.loads(r_3.content)
        data_main = data['main']
        data_weather = data['weather'][0]
        data_temp = data_main['temp']
        data_temp -= 273
        # print(f"Погода: {data_weather['main']}")
        # print(f"Тепмература по цельсию: {data_temp} градусов")
        return [data_temp, data_weather['main']]

    def set_weather_city(self, coords):
        return self.__get_weather(coords)


# get - будет вызываться в сет, в сет передаем координаты, которые потом передаем в гет.
# затем выводим на экран любую вводную инфу о погоде(поиграться с диктами, посмотреть, что есть в json строке, которую мы получаем)

# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

