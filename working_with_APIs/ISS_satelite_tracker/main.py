# making a ISS satellite tracker based on your location


import requests
import smtplib, ssl
from datetime import datetime
import time

# constants for email SMTP gmail

password = "gbfyommpspjqgfek"
sender_email = "devrumaan@gmail.com"

# multiple reciver emails can be in a form of a list

receiver_email = ["devrumaan@gmail.com"]
message = """\
Subject: Hi Love

This message is sent from Rumaan from his python program . The ISS satellite is in the sky above your house , find it"""

MY_LAT = 13.0230651  # Your latitude
MY_LONG = 77.649095  # Your longitude


# calling the ISS tracker API and reciveing he coordinates of the ISS tracker and checking if
# its close to our current coordinates


def is_close():
    """Your position is within +5 or -5 degrees of the ISS position."""

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"current location of the ISS Satellite: latitutde={iss_latitude} , longtitude = {iss_longitude}")

    lesslat = MY_LAT - 5
    morelat = MY_LAT + 5
    lesslong = MY_LONG - 5
    morelong = MY_LONG + 5
    if lesslat <= iss_latitude <= morelat and lesslong <= iss_longitude <= morelong:
        return True
    else:
        return False


##making sure we know the sunset and sunrise dates and times by calling the
##sunset API using our latitude and longitude coordinates

def is_night():
    """checks for nightime at you current location"""
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

    time_now = datetime.now().hour

    if time_now > sunset < sunrise:
        return True


def mail(sender_email, password, message):
    """sends a notification mail to you if the ISS is in the sky"""
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(sender_email, password)
    connection.sendmail(sender_email, receiver_email, message)


# If the ISS is close to my current position
its_here = is_close()
print(its_here)
# and it is currently dark
if is_night():
    print("its dark")

# Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    if its_here and is_night:
        mail(sender_email, password, message)

# readlines.open()
