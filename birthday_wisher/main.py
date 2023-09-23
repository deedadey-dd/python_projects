import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "deedadey@vivaldi.net"
MY_PASSWORD = '"Dee.Chri5t!'

# #################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
with open("./birthdays.csv") as add_data:
    all_data = pandas.read_csv(add_data)
    birthdays = all_data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
present_month = today.month
present_day = today.day
letter = ""

msg = random.randint(1, 3)
if msg == 1:
    letter = "./letter_templates/letter_1.txt"
elif msg == 2:
    letter = "./letter_templates/letter_2.txt"
else:
    letter = "./letter_templates/letter_3.txt"


for person in birthdays:
    if person["month"] == present_month and person["day"] == present_day:
        your_mail = person["email"]
        your_name = person["name"]

        with open(letter, mode="r") as file:
            old_letter = file.read()

        modified_letter = old_letter.replace("[NAME]", f"{person['name'].title()}")
        # print(modified_letter)

        with smtplib.SMTP("smtp.vivaldi.net", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=f"{your_mail}", msg=f"{modified_letter}")


# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
