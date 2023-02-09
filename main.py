from twilio.rest import Client
import requests

# 38.984852,-77.092690
account_sid = "AC2e16b6645b3eba312c62f4d83b4c89fc"
auth_token = "80e327bbd2f3e596e710d1ee3b1d00d3"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "ff59651ffaf8162c121c202972ae6ac0"

parameters = {
    "lat": 8.373140,
    "lon": -62.642799,
    "exclude": ["current","minutely","daily"],
    "appid": api_key,
}

response = requests.get(url=OWM_Endpoint, params=parameters)

response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][0:12]
will_rain = False

for hour in hourly_data:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today. Bring an umbrella along today.",
                from_="+19705572846",
                to="+12404255697")

    print(message.status)


