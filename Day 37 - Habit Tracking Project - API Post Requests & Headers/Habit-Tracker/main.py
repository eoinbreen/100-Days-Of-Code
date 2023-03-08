import requests

USERNAME = "eoinbreen"
TOKEN = "12345678"
GRAPH_ID = "steps"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params) # Creating Username


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Step Counter",
    "unit": "Steps",
    "type": "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# requests.post(url=graph_endpoint, json=graph_params, headers=headers)  # Creating Grid

html_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

html_params = {
    "date": "20230306",
    "quantity": "12655"
}

response = requests.post(url=html_endpoint, json=html_params, headers=headers)
print(response.text)
# https://pixe.la/v1/users/eoinbreen/graphs/steps






