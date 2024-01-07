from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

selenium_path = 'C:\Development\chromedriver.exe'

driver = webdriver.Chrome(service=Service(executable_path=selenium_path))

driver.get('https://en.wikipedia.org/wiki/Main_Page')

count_div = driver.find_element(By.ID, 'articlecount')
article_count = count_div.find_element(By.TAG_NAME, 'a')
print(article_count.text)
# article_count.click()


# click a link
# history_link = driver.find_element(By.LINK_TEXT, 'View history')
# history_link.click()

search_box = driver.find_element(By.NAME, 'search')
search_box.send_keys('Python')
search_box.send_keys(Keys.ENTER)

time.sleep(10)
