import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time

dubizzle_base_url = 'https://uae.dubizzle.com/motors/used-cars'
chrome_url = 'C:\Development\chromedriver.exe'

# Get user's input and store them within the following variables
city = ''
make = 'Mercedes-Benz'
model = 'C-Class'
price1 = '1'
price2 = '500000'
year1 = '1920'
year2 = '2025'
kilos1 = '0'
kilos2 = '100000'

# begin constructing the url with the make and model
features = [make, model]
dubizzle_url = dubizzle_base_url
for feature in features:
    if feature != '':
        dubizzle_url += f'/{feature.lower()}/?'

# If there are more filters, add them to the url as follows.
# # In hindsight, the list below was unnecessary since the variables could have been referred to directly.

filters = [price1, price2, year1, year2, kilos1, kilos2]

if filters[0] and filters[1] != '':
    dubizzle_url += f'price__gte={price1}&price__lte={price2}'

if filters[2] != '':
    dubizzle_url += f'&year__gte={year1}'

if filters[5] != '':
    dubizzle_url += f'&kilometers__lte={kilos2}'

if filters[3] != '':
    dubizzle_url += f'&year__lte={year2}'
if filters[4] != '':
    dubizzle_url += f'&kilometers__gte={kilos1}'

print(dubizzle_url)
driver = webdriver.Chrome(service=Service(executable_path=chrome_url))
driver.get(url=dubizzle_url)
time.sleep(60)






