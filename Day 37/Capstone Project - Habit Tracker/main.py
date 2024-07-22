import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("TOKEN"),
    "username": os.getenv("USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{os.getenv("USERNAME")}/graphs"

graph_config = {
    "id": os.getenv("GRAPH_ID"),
    "name": "Indoor Cycling",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": os.getenv("TOKEN"),
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{graph_endpoint}/{os.getenv("GRAPH_ID")}"
today = datetime.now()

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

# response = requests.post(url=post_endpoint, json=post_params, headers=headers)
# print(response.text)

# Updating a previous post
day = datetime(year=2024, month=7, day=21).strftime("%Y%m%d")

update_endpoint = f"{post_endpoint}/{day}"

update_params = {
    "quantity": "10",
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

# Deleting a post
delete_endpoint = f"{post_endpoint}/{day}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
