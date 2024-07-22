import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
MY_LAT = 19.075983
MY_LONG = 72.877655

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": os.getenv("API_KEY"),
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella.",
        from_='+12566699553',
        to='+918218827422'
    )
    print(message.status)


