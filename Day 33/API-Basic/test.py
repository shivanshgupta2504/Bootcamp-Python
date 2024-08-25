import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # for raising HTTP error

data = response.json()
print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)
