import requests
import datetime 

USERNAME = "tangel"
TOKEN = "mj7hsdfvj2kug3mhg7"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    # "token": TOKEN,
    # "username": USERNAME,
    # "agreeTermsOfService": "yes",
    # "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
} 

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ..........Adding a pixel to the graph
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": datetime.datetime.now().strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# ..........Updating a pixel on the graph
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime.datetime.now().strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "20",
}   
# response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Update yesterday's pixel
yesterday_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d")
yesterday_pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_date}"
yesterday_pixel_data = {
    "quantity": "25",
}   
# response = requests.put(url=yesterday_pixel_update_endpoint, json=yesterday_pixel_data, headers=headers)
# print(f"Yesterday Update{response.text}")

# ..........Deleting a pixel on the graph
# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime.datetime.now().strftime('%Y%m%d')}"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)