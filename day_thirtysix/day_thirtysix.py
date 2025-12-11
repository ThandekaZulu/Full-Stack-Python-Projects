import requests
from requests.auth import HTTPBasicAuth

# --- Weather API setup ---
api_key = "439d0af2d15ac6714047fb80b727e383"
lat = -29.155055   # Mandeni latitude
lon = 31.407762    # Mandeni longitude

url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4,
    "units": "metric"
}

response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json()

# --- Check if rain is forecasted ---
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:  # codes <700 = rain/snow/etc.
        will_rain = True

# --- Send SMS via BulkSMS if rain is detected ---
if will_rain:
    sms_url = "https://api.bulksms.com/v1/messages"
    payload = {
        "to": "+27812593341",  # replace with your SA number
        "body": "🌧️ It's going to rain today in Mandeni. Don't forget your umbrella ☔️"
    }
    # Use your BulkSMS account credentials
    response = requests.post(
        sms_url,
        json=payload,
        auth=HTTPBasicAuth("tangel", "20603261Tsa")
    )
    print(response.json())
else:
    print("No rain today, SMS not sent.")
