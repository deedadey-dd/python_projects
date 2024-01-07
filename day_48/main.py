from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


google_chrome_url = 'C:\Development\chromedriver.exe'

driver = webdriver.Chrome(service=Service(executable_path=google_chrome_url))

website_url = 'https://www.python.org/'
driver.get(website_url)

calendar_div = driver.find_element(By.CLASS_NAME, 'event-widget')
# heading = calendar_div.find_element(By.CSS_SELECTOR, 'h2.widget-title')
# print(heading.text)

events = calendar_div.find_elements(By.TAG_NAME, 'li')
# print(events)
# print(events[0].text.split('\n'))


# LONG FORMAT STYLE
event_dict = {}
for num in range(0, len(events)):
    single_event = events[num].text.split('\n')
    mini_event = {
        'time': single_event[0],
        'name': single_event[1],
    }
    event_dict[num] = mini_event

print(event_dict)

# DICTIONARY COMPREHENSION STYLE
event_dict = {} # this line is just to clear the content of the dictionary and is not needed in this style.
event_dict = {num: {'time': events[num].text.split('\n')[0], 'name': events[num].text.split('\n')[1]}
              for num in range(0, len(events))}

print(event_dict)


# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# chrome_driver_path = "C:\Development\chromedriver.exe"
# driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))
#
# driver.get('https://www.amazon.com/VIZIO-Chromecast-Mirroring-Streaming-Channels/dp/B092Q1TRJC/'
#            'ref=sr_1_2?crid=3EUS0DA9JLXQS&keywords=42+inch+smart+tv&qid=1698293366&sprefix=42%2Caps%2C912&sr=8-2')
#
# currency_symbol = driver.find_element(by=By.CLASS_NAME, value='a-price-symbol').text
# whole_price = driver.find_element(by=By.CLASS_NAME, value='a-price-whole').text
# fraction_price = driver.find_element(by=By.CLASS_NAME, value='a-price-fraction').text
#
# price = f'{currency_symbol}{whole_price}.{fraction_price}'
# print(price)
#
#
# #
# # time.sleep(150)
# # driver.close()
# driver.quit()
