import requests
from twilio.rest import Client

API_KEY = #Insert your open weater map API key
MY_LAT =  # Your latitude
MY_LONG =  # Your longitude
END_POINT = "https://api.openweathermap.org/data/2.5/forecast"

# twilio credentials
account_sid = # Your twilio account_sid 
auth_token = # Your twilio auth_token

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}
today_data = []

response = requests.get(END_POINT, params=params)
print(response.raise_for_status())
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])

for hour_data in weather_data["list"]:
    today_data.append(hour_data["weather"][0]["id"])

will_rain = False
for data in today_data:
    if data < 700:
        will_rain = True

client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages \
        .create(
        body="It's going to rain today. Remember an umbrella ☂️",
        from_='', #Insert your twilio generated phone number
        to='' #Insert your verified twilio phone number 
    )
    print(message.status)
else:
    message = client.messages \
        .create(
        body="No rain today. Enjoy the weather ☀️",
        from_='', #Insert your twilio generated phone number
        to='' #Insert your verified twilio phone number 
    )
    print(message.status)
