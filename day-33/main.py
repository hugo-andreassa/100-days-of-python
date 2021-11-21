import requests
import datetime

# ISS Location ----------------------------------------------------------------
# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# lat = data["iss_position"]["latitude"]
# long = data["iss_position"]["longitude"]
#
# iss_position = (lat, long)
#
# print(iss_position)


# Sunset Time -----------------------------------------------------------------
parameters = {
    "lat": -23.710220,
    "lng": -46.412670,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(data)
