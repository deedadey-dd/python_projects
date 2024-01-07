import requests
import smtplib


MY_EMAIL = 'deedadey@gmail.com'
MY_PASSWORD = '"Dee.Chri5t!'


class NotificationManager:
    def __init__(self, message):
        self.SHEET_URL = 'https://api.sheety.co/2ca53f58a7655a73fd473d0607e391fa/flightDeals/users'
        self.response = requests.get(url=self.SHEET_URL)
        self.user_data = self.response.json()

        self.data = {
          'recipient[]': ['0205448044'],
          'sender': 'Dee Code',
          'message': message.encode('utf-8'),
        }

    def send_sms(self):
        sms_endpoint = 'https://api.mnotify.com/api/sms/quick'
        sms_apikey = 'Tasah4pRyrxSKuXYkst5nyBtC'

        sms_url = sms_endpoint + '?key=' + sms_apikey
        requests.post(sms_url, self.data)
        print('sms sent')

    def send_email(self):

        for person in range(len(self.user_data['users'])):
            your_email = self.user_data['users'][person]['email']

            with smtplib.SMTP(host="smtp.vivaldi.net", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=f'{your_email}', msg=f"Subject: FLIGHT ALERTS!!!"
                                                                                      f"\n\n {self.data['message']}")
                print('email sent')
