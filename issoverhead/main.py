import requests
from datetime import datetime
import smtplib, time

MY_LAT = 5.102650 # Your latitude
MY_LONG = -1.332770 # Your longitude
MARGIN = 5
MY_EMAIL = "deedadey@vivaldi.net"
MY_PASSWORD = '"Dee.Chri5t!'
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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

print(f"Sunrise: {sunrise}\nSunset: {sunset}\nPresent: {time_now}")
print(f"ISS Location: ({iss_longitude}, {iss_latitude})")
print(f"My Location: ({MY_LONG}, {MY_LAT})")

print(f"LONG DIFF: {abs(iss_longitude - MY_LONG)}")
print(f"LAT DIFF: {abs(iss_latitude - MY_LAT)}")

# If the ISS is close to my current position
# and it is currently dark
while True:
    time.sleep(60)
    if ((abs(iss_latitude - MY_LAT) <= MARGIN and abs(iss_longitude - MY_LONG) <= 5) and
            (time_now < sunrise or time_now > sunset)):
        with smtplib.SMTP("smtp.vivaldi.net", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="deedadey@gmail.com",
                                msg="Subject: ISS is Passing\n\nLift up Your Eyes and find the Satellite passing.")

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



