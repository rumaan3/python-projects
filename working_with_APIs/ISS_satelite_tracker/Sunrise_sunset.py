# making a ISS satellite tracker based on your location

##first making sure we know the sunset and sunrise dates and times by calling the
##sunset API using our latitude and longitude coordinates


import requests
from datetime import datetime

MY_LAT = 13.023065
MY_LONG = 77.649095

LatLng = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

sun = requests.get("https://api.sunrise-sunset.org/json", params=LatLng)
sun.raise_for_status()
sunjson = sun.json()

sunrise = sunjson["results"]["sunrise"]
sunrise = sunrise.split("T")[1].split("+")[0]
sunset = sunjson["results"]["sunset"]
sunset = sunset.split("T")[1].split("+")[0]
# golden = sunjson["results"]["golden_hour"]

# print(f"sunrise = {sunrise}, sunset = {sunset}, golden hour  = {golden}")
print(f"sunrise = {sunrise}, sunset = {sunset}")
# print(sunjson)

time_now = datetime.now()

print(f"current = {time_now}")
