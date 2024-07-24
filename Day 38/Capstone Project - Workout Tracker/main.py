import requests
import os
from dotenv import load_dotenv
from datetime import datetime

GENDER = "male"
AGE = 22
WEIGHT = 101
HEIGHT = 172

load_dotenv()

nutritionix_headers = {
    "x-app-id": os.getenv("NUTRITIONIX_API_ID"),
    "x-app-key": os.getenv("NUTRITIONIX_API_KEY"),
    "Content-Type": "application/json"
}

auth_headers = {
    "Authorization": os.getenv("AUTH"),
    "username": os.getenv("USERNAME"),
    "password": os.getenv("PASSWORD"),
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_post_endpoint = "https://api.sheety.co/80ffa7bcd1753f1374c34ef00773fec9/myWorkouts/workouts"

query = input("Tell me what you did today: ")

nutritionix_params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)
response.raise_for_status()

result = response.json()
# print(result["exercises"][0]['name'])
print(result)
# exercise = result["exercises"][0]['name']
# duration = result["exercises"][0]['duration_min']
# calories = result["exercises"][0]['nf_calories']

# print(f"Exercise: {exercise}, Duration: {duration}, Calories: {calories}")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=sheety_post_endpoint,
        json=sheet_inputs,
        headers=auth_headers
    )

    print(sheet_response.text)


