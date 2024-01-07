import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_url = 'C:\Development\chromedriver.exe'

driver = webdriver.Chrome(service=Service(executable_path=chrome_url))

driver.get('https://orteil.dashnet.org/cookieclicker/')

# Wait for Language choices to be ready and click English
wait = WebDriverWait(driver, 15)
language = wait.until(EC.presence_of_element_located((By.ID, 'langSelect-EN')))

# Find and click allow website cookies 'Got it' Button
website_cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
website_cookies.click()
# Now you can interact with the element
language.click()



# cookie_button = wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))


# def click_cookie():
#     # cookie_button = driver.find_element(By.ID, 'bigCookie')
#     cookie_button = wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))
#     while True:
#         cookie_button.click()  # click_cookie(cookie_button)
#
#
# def check_cookie_number():
#     cookie_number = driver.find_element(By.ID, 'cookies')
#     while True:
#         # cookie_number = driver.find_element(By.ID, 'cookies')
#         time.sleep(5)
#         cookies_info = cookie_number.text
#         cookies = int(cookies_info.split('\n')[0].split()[0])
#         print(cookies)

# website_cookies = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cc_btn_accept_all")))
# website_cookies.click()

def click_cookie():
    cookie_button = wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))

    while True:
        cookie_button.click()


# click_cookie(cookie_button)

def check_cookie_number():

    while True:
        time.sleep(5)
        cookie_number = driver.find_element(By.ID, 'cookies').text

        cookies_string = cookie_number.split('\n')[0].split()[0]
        cookies_info = cookies_string.replace(',', '')
        cookies = int(cookies_info)
        print(cookies)
        wait.until(EC.presence_of_element_located((By.ID, "productPrice0")))
        # product_name = ['Cursor', 'Grandma', 'Farm', 'Mine', 'Factory', 'Bank', 'New_Product_1', 'New_Product_2']
        # products = {}
        # for x in range(0, 8):
        #     product_id = 'productName' + str(x)
        #     name = product_name[x]
        #     product_price = 'productPrice' + str(x)
        #     price_str = driver.find_element(By.ID, f'{product_price}').text
        #     price = price_str.replace(',', '')
        #     mini_product = {
        #         'name': product_name[x],
        #         'price': price,
        #     }
        #
        #     products[x] = mini_product
        # # wait.until(EC.presence_of_element_located((By.ID, "productPrice0")))
        # print(products)
        # print(int(products[0]['price']))  # conversion to integer for comparison
        # item_to_buy = ''
        # largest_price = 0
        # for item in products.values():
        #
        #     if item['price'] != '':
        #         current_price = int(item['price'])
        #     else:
        #         current_price = 0
        #
        #     name = item['name']
        #
        #     if cookies >= current_price > largest_price:
        #         largest_price = current_price
        #         item_to_buy = name
        # index_to_buy = product_name.index(item_to_buy)
        # buy_item = driver.find_element(By.ID, f'product{index_to_buy}')
        # print(f'product{index_to_buy}')
        # print(f'largest price: {largest_price}')
        # buy_item.click()
        product_prices = []

        for x in range(0, 20):
            new_price_str = driver.find_element(By.ID, f'productPrice{x}').text
            new_price = new_price_str.replace(',', '')
            if new_price != '':
                product_prices.append(new_price)
        print(product_prices)

        largest_price = -1
        item_to_buy = ''
        # item_code = -1

        for y in range(0, len(product_prices)):
            if cookies > int(product_prices[y]) > largest_price:
                largest_price = int(product_prices[y])
                item_to_buy = f'product{y}'
                # item_code = y

        # buy_item = driver.find_element(By.ID, item_to_buy)
        buy_item = wait.until(EC.presence_of_element_located((By.ID, item_to_buy)))
        buy_item.click()
        print(item_to_buy)


thread2 = threading.Thread(target=click_cookie)
thread1 = threading.Thread(target=check_cookie_number)


thread2.start()
thread1.start()

thread1.join()
thread2.join()

