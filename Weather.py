import requests
import datetime
from pprint import pprint

open_weather_token = "5611df5fd081b8985d2eb8da8da7c243"

def get_weather(city, open_weather_token):
    try:
        r1 = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={open_weather_token}&units=metric")
        data = r1.json();
        #pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        cur_humidity = data["main"]["humidity"]
        cur_pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(f"{city}\n")
        print(f"temperature: {cur_weather}")
        print(f"humidity: {cur_humidity}")
        print(f"pressure: {cur_pressure}")
        print(f"wind: {wind}")
        print(f"sunrise: {sunrise}")
        print(f"sunset: {sunset}")

        print(f"\n\nHave a nice day!")

    except Exception as ex:
        print(ex)
        print("check city name")


def main():
    city = "Zhukovsky" #input("input city: ")
    get_weather(city, open_weather_token)
    city = input("")

if __name__ == '__main__':
    main()