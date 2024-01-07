import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


dubizzle_base_url = 'https://uae.dubizzle.com/motors/used-cars'

# this must go into env variables because it contains private api information

# sheety_url = 'https://api.sheety.co/2ca53f58a7655a73fd473d0607e391fa/tonaton/mercedes'
#
# google_form_url = ('https://docs.google.com/forms/d/e/1FAIpQLSdqGhhJQZ96TlkXgc8tC5ahkRigRWPF6'
#                    'NCIdf8UcaO-Gw7-VA/viewform?usp=sf_link')

chrome_url = 'C:\Development\chromedriver.exe'

driver = webdriver.Chrome(service=Service(executable_path=chrome_url))
driver.get(url=dubizzle_base_url)

input_element = driver.find_element(By.CSS_SELECTOR, "input[data-testid='category_1_input']")

# Perform actions on the input element (e.g., get its value)
element_value = input_element.get_attribute("Mercedes-Benz")
wait = WebDriverWait(driver, 15)


dubizzle_response = requests.get(url=dubizzle_base_url)

