import requests
from twilio.rest import Client
import os

# api_key = "758cf993b08669d2a43d5b247c9ec85c"
# # api_key = os.environ.get("WEATHER_API_KEY")
# account_sid = "AC497d8acfa141d3c0643aa28a74329db7"
# auth_token = "b1b3a09696d646316ef34996ae22681a"
MY_LAT = 19.075983
MY_LONG = 72.877655

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella.",
        from_='+12566699553',
        to='+918218827422'
    )
    print(message.status)


