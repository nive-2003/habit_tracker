import requests
from datetime import datetime

USERNAME = "nive"
TOKEN = "fwegjwngrinwgrk24"
pixels_endPoint = "https://pixe.la/v1/users"

# Create a new graph
graph_endpoint = f"{pixels_endPoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment the following lines if you want to create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
# Add a new pixel to the graph
pixel_creation_endpoint = f"{pixels_endPoint}/{USERNAME}/graphs/graph1"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixels_endPoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "3"
}

# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint = f"{pixels_endPoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)