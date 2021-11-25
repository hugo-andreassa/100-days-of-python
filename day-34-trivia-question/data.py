import requests

AMOUNT = 10
TYPE = "boolean"

response = requests.get(f"https://opentdb.com/api.php?amount={AMOUNT}&type={TYPE}")
response.raise_for_status()
data = response.json()["results"]

question_data = data
