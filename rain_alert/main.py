import requests
from twilio.rest import Client

account_sid = 'ACa9228a24ab57e01084b77f957fbe8fead'
auth_token = '88e54d6820c268ceaafc34b701f5ae3dd'


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "a1332833f062e1fc75b25e8799286743"

MY_LAT = 56.461430
MY_LONG = -2.968110


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)

response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour in range(0, 12):
    condition = weather_data["hourly"][hour]["weather"][0]["id"]
    if condition < 700:
        # print(f"You will need an umbrella at hour: {hour}.")
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
                from_='+17409001474',
                body='It is going to rain today. Remember to take an umbrella ☔️',
                to='+233205448044',
                )
    print(message.status)

