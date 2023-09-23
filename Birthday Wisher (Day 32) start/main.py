import random
import smtplib

#
my_email = 'deedadey@vivaldi.net'
my_password = '"Dee.Chri5t!'
#
# with smtplib.SMTP("smtp.vivaldi.net", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#
#     connection.sendmail(from_addr=my_email, to_addrs="deedadey@yahoo.co.uk", msg="Subject: Python STMP Library"
#                                                                                  "\n\nThis is another email from Python")

import datetime as dt
import smtplib

now = dt.datetime.now()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

year = now.year
day = weekdays[now.weekday()]

with open("quotes.txt") as file:
    messages = file.readlines()
    message = messages[random.randint(0, len(messages) - 1)]

if day == "Thursday":
    with smtplib.SMTP("smtp.vivaldi.net", 587) as connect:
        connect.starttls()
        connect.login(user=my_email, password=my_password)
        connect.sendmail(
            from_addr=my_email,
            to_addrs="deedadey@gmail.com",
            msg=f"Subject:Motivational {day}\n\n{message}")

# date_of_birth = dt.datetime(year=1987, month=1, day=25, hour=5)
# print(date_of_birth)
