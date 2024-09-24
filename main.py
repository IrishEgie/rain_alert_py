import requests as rq
from config import *
from twilio.rest import Client
from datetime import datetime as dt
import smtplib

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

def send_email():
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=EMAIL_APP_PASS)
        connection.sendmail(from_addr=EMAIL,to_addrs=send_to, msg="Subject: Weather Today\n\nHigh chances of rain today, don't forget to bring an umbrella")
    print(f"Email sent to {send_to} on {dt.now()}")

response = rq.get(f"https://api.openweathermap.org/data/2.5/forecast?", params=weather_param)
response.raise_for_status()

weather_data = response.json()["list"]
half_day_forecast = [hour["weather"][0]["id"] for hour in weather_data] #this is a new list

for weather_code in half_day_forecast:
    if int(weather_code) < 700:
        print("Probable Rain detected, Please bring an umbrella⛱")
        send_email()
        break
# print(half_day_forecast)