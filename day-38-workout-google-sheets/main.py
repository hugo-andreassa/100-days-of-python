import requests
from datetime import date, datetime

API_NUTRI_URL = "https://trackapi.nutritionix.com/"
API_SHEET_URL = "https://api.sheety.co/dfba959c9fc7d64f75d73a39ef8ac16e/myWorkouts/workouts"

APPLICATION_ID = "2c4ce77c"
API_NUTRI_KEY = "9b56c1d7164bb6f65f5ce28ffa9fb1b1"


def parse_exercises_to_json_via_nutri_api(exercises: str) -> [str]:
    nutri_headers = {
        "x-app-id": APPLICATION_ID,
        "x-app-key": API_NUTRI_KEY,
        "x-remote-user-id": "0"
    }
    nutri_params = {
        "query": exercises
    }

    response = requests.post(f"{API_NUTRI_URL}/v2/natural/exercise", json=nutri_params, headers=nutri_headers)
    response.raise_for_status()
    return response.json()["exercises"]


def save_exercise_to_google_sheet(exercise: str, duration: int, calories: int):
    today = datetime.today()

    sheet_params = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories
        }
    }
    response = requests.post(API_SHEET_URL, json=sheet_params)
    response.raise_for_status()
    # print(response.text)


exercises = input("Tell me which exercise do you did: ")

nutri_data = parse_exercises_to_json_via_nutri_api(exercises)
for item in nutri_data:
    save_exercise_to_google_sheet(item["user_input"], item["duration_min"], item["nf_calories"])
