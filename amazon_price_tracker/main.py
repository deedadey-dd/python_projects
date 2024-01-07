import urllib.request
from pprint import pprint
from bs4 import BeautifulSoup
import requests


PRODUCT_URL = ('https://www.amazon.com/VIZIO-Chromecast-Mirroring-Streaming-Channels/dp/B092Q1TRJC/ref=sr_1_4?cr'
               'id=3G8OJ06K4MI4X&keywords=60+inch+smart+tv&qid=1698114776&sprefix=60+%2Caps%2C352&sr=8-4')
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
BARGAIN_PRICE = 140.00
# TODO Create a beautiful soup and extract the price of the item.
# response = requests.get(url=PRODUCT_URL, headers=)
# response = urllib.request.urlopen(PRODUCT_URL)

response = requests.get(url=PRODUCT_URL, headers=HEADER)
webpage = response.text

# sess = dryscrape.Session(base_url='https://www.amazon.com')
# sess.visit(PRODUCT_URL)
# sess.set_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) '
#                               'Chrome/54.0.2840.71 Safari/537.36')
# webpage = sess.body()
print(webpage)
soup = BeautifulSoup(webpage, 'html.parser')
print(soup)
price_whole = soup.find(name='span', class_='a-price-whole')
price_fraction = soup.find(name='span', class_='a-price-fraction')

print(f'Price: ${price_whole}.{price_fraction}')

# TODO Create a condition that sends an email or SMS alert when the condition is met
# Condition = if price falls below your bargain price
