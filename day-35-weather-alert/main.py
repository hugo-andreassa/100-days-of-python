import requests
import datetime as dt
from twilio.rest import Client


def send_message(text: str):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body=text,
        from_='+19704429461',
        to='+5511956492900'
    )
    print(message.sid)


ACCOUNT_SID = "AC6d2792e2305e4384c2ecc9e2982a8f71"
AUTH_TOKEN = "bc0b2c5214862c18e33bd0d93b41adcf"

API_URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "e25524980719884b75610befdb27c926"
LAT = "-23.71065855535232"
LONG = "-46.41273176149347"

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "units": "metric",
    "lang": "pt_br",
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(API_URL, params=weather_params)
response.raise_for_status()
json_data = response.json()

hourly_data = json_data["hourly"][:48]
will_rain = False

for data in hourly_data:
    weather_data = data["weather"][0]

    if weather_data["id"] < 700:
        will_rain = True
        # datetime = dt.datetime.fromtimestamp(data["dt"]).strftime("%d/%m/%Y %Hh")
        # send_message(f"Bring an umbrella. It's going to rain at {datetime}")

if will_rain:
    message = f"Bring an umbrella. It's going to rain at the next 12 hours! ☂"
    send_message(message)
    # print(message)
