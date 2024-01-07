import requests

endPoint = 'https://api.mnotify.com/api/sms/quick'
apiKey = 'Tasah4pRyrxSKuXYkst5nyBtC'

data = {
  'recipient[]': ['0265550354', '0205448044', '0544706637'],
  'sender': 'CCI',
  'message': 'API messaging is fun!',
}
url = endPoint + '?key=' + apiKey
print(url)
response = requests.post(url, data)
print(response.status_code)
data = response.json()
print(data)
