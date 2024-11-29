import requests
from datetime import datetime

API_KEY = "f07e8589b499585c0e0a2c851e807277"
APP_ID = "933f0efb"

weight = 100
height = 182.88
age = 28

today = datetime.now().date()
date = today.strftime("%d/%m/%Y")
time = datetime.now().time()
time = time.strftime("%H:%M:%S")

# print(time)

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

params = {
    "query": input("enter what you did"),
    # "query": "badminton for 5 hours",
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
}
URL = "https://trackapi.nutritionix.com"
# URL_Sheets_Get = "https://api.sheety.co/d830c1db448916487119ddaed160ea99/workoutTracker/workouts"
URL_Sheets_Post = "https://api.sheety.co/d830c1db448916487119ddaed160ea99/workoutTracker/workouts"

request_endpoint= f"{URL}/v2/natural/exercise"

response = requests.post(url=request_endpoint,json=params, headers=headers)
print(response)
print(response.text)
exercise_data = response.json()

activity = exercise_data["exercises"][0]["name"]
duration = exercise_data["exercises"][0]["duration_min"]
calories = exercise_data["exercises"][0]["nf_calories"]

post_data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": activity.title(),
        "duration":duration,
        "calories": calories,
    }
}

# print(post_data)
response_add = requests.post(url=URL_Sheets_Post, json=post_data, headers=headers )
print(response_add)
print(response_add.text)
