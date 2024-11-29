from twilio.rest import Client
import requests

account_sid = 'AC95adf65f9fab22d767348a94c7a324f2'
auth_token = '341cf824ed29ec68738fc65f49441e43'
client = Client(account_sid, auth_token)

api_key= "45e3d6cef419f99a7ed5338b87f28b53"
LAT=13.0056192
LONG=77.6536064
api_call=f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LONG}&cnt=4&appid={api_key}"

response = requests.get(api_call)
weather_data = response.json()

flag = False

for hour_data in weather_data["list"]:
    id = hour_data["weather"][0]["id"]
    if id < 700:
        flag = True

if flag == False:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Bring an Umbrella',
        to='whatsapp:+917411939565'
    )

    print(message.sid)

