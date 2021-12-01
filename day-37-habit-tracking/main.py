import requests
from datetime import datetime, date

USERNAME = "hugoandreassa"
TOKEN = "sfHNcIBnPRF4"
GRAPH_ID = "graph1"

PIXELA_API = "https://pixe.la/v1/users"

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(PIXELA_API, json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Coding Graph",
#     "unit": "Commit",
#     "type": "int",
#     "color": "kuro"
# }
# response = requests.post(f"{PIXELA_API}/{USERNAME}/graphs", json=graph_params, headers=headers)
# print(response)

# pixel_params = {
#     "date": date.today().strftime("%Y%m%d"),
#     "quantity": "1"
# }
# response = requests.post(f"{PIXELA_API}/{USERNAME}/graphs/{GRAPH_ID}", json=pixel_params, headers=headers)
# print(response)

pixel_update_params = {
    "quantity": "100"
}
response = requests.put(f"{PIXELA_API}/{USERNAME}/graphs/{GRAPH_ID}/{date.today().strftime('%Y%m%d')}",
                        json=pixel_update_params, headers=headers)
print(response)

print(f"{PIXELA_API}/{USERNAME}/graphs/{GRAPH_ID}")
