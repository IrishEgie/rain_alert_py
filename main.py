import requests as rq
from config import *


weather_param = {
    "lat": 11.589979,
    "lon": 124.986818,
    "appid": api_key,
    "cnt": 4,
}
response = rq.get(f"https://api.openweathermap.org/data/2.5/forecast?", params=weather_param)
response.raise_for_status()

weather_data = response.json()["list"]
half_day_forecast = [hour["weather"][0]["id"] for hour in weather_data] #this is a new list
for weather_code in half_day_forecast:

    if int(weather_code) < 700:
        print("Probable Rain detected, Please bring an umbrella")
# print(half_day_forecast)