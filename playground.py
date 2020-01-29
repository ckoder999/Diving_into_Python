import requests
import pprint
#from dateutil.parser import parse
import datetime

class YahooWeatherForecast():
    def __init__(self, city):
        self.city = city

    def get(self):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={self.city},ru&units=metric&lang=ru&APPID=334739ed0b81c466c0cfabc4db98e5cb"
        data = requests.get(url).json()
        forecast_data = data["list"] #dt_txt  - date time is given
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": datetime.datetime.fromtimestamp(day_data["dt"]).strftime('%Y-%m-%d %H:%M:%S'),
                "high_temp": day_data["main"]["temp_max"]
            })
        print(forecast)


ywp = YahooWeatherForecast("Moscow")

ywp.get()
