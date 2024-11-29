import requests
from datetime import datetime,date



URL = "https://pixe.la/v1/users"
USERNAME = "devrumaan"
TOKEN = "211s3e1231s12w12w"
GRAPHID = "cyclegraph1"
TODAY = datetime.now().date()
TODAY = str(TODAY.strftime("%Y%m%d"))
KMS = "30"

print(TODAY)

headers = {
    "X-USER-TOKEN": TOKEN,
}


params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes"
}

# response = requests.post(url=URL , json= params)
# print(response.text)

graph_endpoint = f"{URL}/{USERNAME}/graphs"

graph_endpoint_params = {
    "id":GRAPHID ,
    "name": "CyclingGraph",
    "unit": "Km",
    "type": "float",
    "color": "sora",

}

# response = requests.post(url = graph_endpoint, json=graph_endpoint_params, headers= headers)
# print(response.text)

pixel_endpoint_post = f"{URL}/{USERNAME}/graphs/{GRAPHID}"
pixel_endpoint_put = f"{URL}/{USERNAME}/graphs/{GRAPHID}/{TODAY}"
pixel_endpoint_params = {
    "date": TODAY,
    "quantity": KMS,

}

# response = requests.post(url = pixel_endpoint_post, json =pixel_endpoint_params, headers= headers)


response = requests.put(url= pixel_endpoint_put, json=pixel_endpoint_put, headers= headers)


print(response.text)

print(pixel_endpoint_put)
