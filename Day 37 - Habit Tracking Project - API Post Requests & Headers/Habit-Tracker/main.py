import requests

USERNAME = "eoinbreen"
TOKEN = "12345678"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "steps",
    "name": "Step Counter",
    "unit": "Steps",
    "type": "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# https://pixe.la/v1/users/eoinbreen/graphs/steps.html






