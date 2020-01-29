import pprint
import requests
import datetime

class YahooWeatherForecast():

    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},ru&units=metric&lang=ru&APPID=334739ed0b81c466c0cfabc4db98e5cb"
        print("Sending HTTP request")
        data = requests.get(url).json()
        forecast_data = data["list"]
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": datetime.datetime.fromtimestamp(day_data["dt"]).strftime('%Y-%m-%d %H:%M:%S'),
                "high_temp": day_data["main"]["temp_max"]
            })
        self._city_cache[city] = forecast
        return forecast


class CityInfo:
    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or YahooWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


def _main():
    weather_forecast = YahooWeatherForecast()
    for i in range(5):
        city_info = CityInfo("Moscow", weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()


if __name__ == "__main__":
    _main()
