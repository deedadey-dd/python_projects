from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

chrome_url = 'C:\Development\chromedriver.exe'

driver = webdriver.Chrome(service=Service(executable_path=chrome_url))

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys("Dennis")

last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Dadey')

email = driver.find_element(By.NAME, 'email')
email.send_keys('dedadey@gmail.com')
# email.send_keys(Keys.ENTER) #this line uses Enter to automatically activate sign up without clicking the button

sign_up = driver.find_element(By.TAG_NAME, 'button')
sign_up.click()

time.sleep(10)

