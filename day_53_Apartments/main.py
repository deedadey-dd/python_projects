import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

tonaton_url = 'https://tonaton.com/search?query=mercedes&region=ashanti&price_min=25000&price_max=80000'
tonaton_base_url = 'https://tonaton.com'

# this must go into env variables because it contains private api information

sheety_url = 'https://api.sheety.co/2ca53f58a7655a73fd473d0607e391fa/tonaton/mercedes'

google_form_url = ('https://docs.google.com/forms/d/e/1FAIpQLSdqGhhJQZ96TlkXgc8tC5ahkRigRWPF6'
                   'NCIdf8UcaO-Gw7-VA/viewform?usp=sf_link')

chrome_url = 'C:\Development\chromedriver.exe'

driver = webdriver.Chrome(service=Service(executable_path=chrome_url))
# driver.get(url=google_form_url)

wait = WebDriverWait(driver, 15)

tonaton_response = requests.get(url=tonaton_url)
tonaton_soup = BeautifulSoup(tonaton_response.text, 'html.parser')
product_list = tonaton_soup.find_all(name='div', class_='product__container flex')
# print(product_list)


# link = product_list[0].find(name='a')
# print(link.get('href'))

for item in product_list:
    present_time = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    price = item.find(name='span', class_='product__title').text.replace('\n', '').lstrip().rstrip()

    name = item.find(name='p', class_='product__description').text.replace('\n', '').lstrip().rstrip()

    location = item.find(name='p', class_='product__location').text.replace('\n', '').lstrip().rstrip()
    link_element = item.find(name='a')
    link = f"{tonaton_base_url}{link_element.get('href')}"
    tags = item.find(name='div', class_='product__tags')
    other_info = tags.find_all(name='span')

    if len(other_info) > 2:
        use = other_info[0].text.replace('\n', '').lstrip().rstrip()
        gear = other_info[1].text.replace('\n', '').lstrip().rstrip()
        mileage = other_info[2].text.replace('\n', '').lstrip().rstrip()
    elif len(other_info) == 2:
        use = other_info[0].text.replace('\n', '').lstrip().rstrip()
        gear = other_info[1].text.replace('\n', '').lstrip().rstrip()
        mileage = ''
    elif len(other_info) == 1:
        use = other_info[0].text.replace('\n', '').lstrip().rstrip()
        gear = ''
        mileage = ''
    else:
        use = ''
        gear = ''
        mileage = ''

    driver.get(url=google_form_url)
    # form_elements = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/di'
    #                                                                      'v/div/div[2]/div/div[1]/div/div[1]/input')))
    price_element = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]'
                                                  '/div/div[1]/div/div[1]/input')
    name_element = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                 '/div/div[1]/div/div[1]/input')
    location_element = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div'
                                                     '/div/div[2]/div/div[1]/div/div[1]/input')
    used_element = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div'
                                                 '/div[2]/div/div[1]/div/div[1]/input')
    gear_element = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/'
                                                 'div[2]/div/div[1]/div/div[1]/input')
    mileage_element = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div'
                                                    '/div[2]/div/div[1]/div/div[1]/input')
    link_on_forms = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]'
                                                  '/div/div[1]/div/div[1]/input')

    price_element.send_keys(price)
    name_element.send_keys(name)
    location_element.send_keys(location)
    used_element.send_keys(use)
    gear_element.send_keys(gear)
    mileage_element.send_keys(mileage)
    link_on_forms.send_keys(link)
    # form_elements.send_keys(price)
    # CREATE A JSON PAYLOAD FOR SHEETY TO LOAD INTO GOOGLE SHEET.
    data_for_sheet = {
            "mercede": {
                "time": present_time,
                "price": price,
                "name": name,
                "location": location,
                "use": use,
                "gear": gear,
                "mileage": mileage,
                "link": link,
            }
        }

    # print(data_for_sheet)
    # USE SHEETY TO ENTER THE INFORMATION IN THE JSON PAYLOAD INTO GOOGLE SHEET
    # sheety_response = requests.post(url=sheety_url, json=data_for_sheet)
    # print(sheety_response)


