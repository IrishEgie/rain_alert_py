import requests as rq
from config import *
from twilio.rest import Client


def send_sms():
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="High chances of rain today, don't forget to bring an umbrella 🌂",
        from_="+17205752924",
        to=my_num,
    )
    print(message.sid)

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
        print("Probable Rain detected, Please bring an umbrella⛱")
        send_sms()
        break
# print(half_day_forecast)