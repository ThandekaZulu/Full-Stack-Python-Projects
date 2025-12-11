# import requests
# from twilio.rest import Client

# # current weather data for Mandini, South Africa
# # api_key = "439d0af2d15ac6714047fb80b727e383"
# # url = "https://api.openweathermap.org/data/2.5/weather"
# # params = {"q": "Mandini,ZA", "appid": api_key, "units": "metric"}

# # response = requests.get(url, params=params)
# # print(response.json())

# # Mandin Call 5 day / 3 hour forecast data
# # import requests


# # lat = -29.155055 Mandini
# # lon = 31.407762 Mandini
# # rainy day coordinates = Zomba, Malawi
# lat = -15.386210
# lon = 35.319309

# url = "https://api.openweathermap.org/data/2.5/forecast"
# api_key = "439d0af2d15ac6714047fb80b727e383"
# account_sid = "AC5a68ff8c683c52969cbdb002ad9b9395"
# auth_token = "c62085974f30140209b6b7a05720ac01"
# client = Client(account_sid, auth_token)
# params = {
#     "lat": lat,
#     "lon": lon,
#     "appid": api_key,
#     "cnt": 4,
#     # "units": "metric"
# }

# response = requests.get(url, params=params)
# response.raise_for_status()
# weather_data = response.json()
# # print(weather_data["list"][0]["weather"][0]["id"])
# # print(response.status_code)

# will_rain = False
# for hour_data in weather_data["list"]:
#     condition_code = hour_data["weather"][0]["id"]
#     # print(condition_code)
#     if int(condition_code) < 700:
#         will_rain = True

# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body="It's going to rain today. Remember to bring an ☔️",
#         from_="+16185185974",
#         to="+27812593341"
#     )
#     print(message.status)
#     # print("Bring an umbrella")  


