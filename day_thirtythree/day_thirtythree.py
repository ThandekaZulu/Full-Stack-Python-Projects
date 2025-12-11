import requests
from datetime import datetime

MY_LAT = -30.559483
MY_LONG = 22.937506

# ISS Program API Example
# response = requests.get(url= "http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# # 1 ..: Hold on; 2..: Here you go; 3..: Go away; 4..: You screwed up
# # 5...: Server is down; 6..: Unknown error

# latitude = response.json()["iss_position"]["latitude"]
# longitude = response.json()["iss_position"]["longitude"]
# data = (latitude, longitude)
# print(data)

# Sunrise-Sunset API Example
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}   
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# print(sunrise)
# print(sunset)

time_now = datetime.now()
# print(time_now.hour)


# print(response.json())