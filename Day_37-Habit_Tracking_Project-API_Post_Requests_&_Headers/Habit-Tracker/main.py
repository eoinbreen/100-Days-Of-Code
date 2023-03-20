import requests
from datetime import datetime

USERNAME = "eoinbreen"
TOKEN = "12345678"
GRAPH_ID = "steps"


# CREATING THE USER
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params) # Creating Username


# CREATING THE GRAPH

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

# ADDING DATA TO GRAPH

# https://pixe.la/v1/users/eoinbreen/graphs/steps.html
html_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

html_params = {
    "date": "20230308",  # today.strftime("%Y%m%d")
    "quantity": "13650"
}

# response = requests.post(url=html_endpoint, json=html_params, headers=headers)

update_endpoint = f"{html_endpoint}/20230308"
put_params = {
    "quantity": "14000"
}
# response = requests.put(url=update_endpoint, json=put_params, headers=headers)  # PUTTING (UPDATING) A PIXEL
# response = requests.delete(url=update_endpoint, headers=headers)  # DELETING A PIXEL
response = requests.get(url=update_endpoint, headers=headers)  # GETTING DATA FROM A PIXEL
print(response.text)







