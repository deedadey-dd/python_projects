import requests
import datetime

APP_ID = "8fbeab10"
API_KEY = "ae248736376c25b3c1e25cd17858905b"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("What Exercises have you done today?\n"),
    "gender": "male",
    "age": 36,
}

# This picks up the essential information from the natural language you give it
response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
exercise_data = response.json()


num_of_exercises = len(exercise_data["exercises"])
for num in range(0, num_of_exercises):
    # prepare data for entry into sheets
    current = datetime.datetime.now()
    date = current.strftime("%d/%m/%y")
    time = current.strftime("%H:%M:%S")
    exercise = exercise_data["exercises"][num]["name"]
    duration = exercise_data["exercises"][num]["duration_min"]
    calories = exercise_data["exercises"][num]["nf_calories"]

    # print(f"Date: {date}\nTime: {time}\nExercise: {exercise}\nDuration: {duration}\nCalories: {calories}")

    # format of the url = url/api/projectname/sheet_name
    SHEETS_URL = "https://api.sheety.co/2ca53f58a7655a73fd473d0607e391fa/myWorkoutsTracking/workouts"

    data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    posting = requests.post(url=SHEETS_URL, json=data)
    print(f"Exercise Number:{num + 1} -> {posting.status_code}")
