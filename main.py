import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "api key"
account_sid = "account sid"
auth_token = "authentication token"


MY_LAT = 40.282650
MY_LONG = -7.503260

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body= "It's going to rain today. Remember to bring an ☂️",
        from_= "phone number",
        to= "phone number"
    )

    print(message.status)



