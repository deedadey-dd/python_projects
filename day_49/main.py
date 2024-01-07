import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver_path = 'C:\Development\chromedriver.exe'

linkedin_url = ('https://www.linkedin.com/jobs/search/?currentJobId=3744797089&f_AL=true&f_WT=2'
                '&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')

driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get(linkedin_url)

wait = WebDriverWait(driver, 10)
begin_sign_in = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')))
begin_sign_in.click()

# Login to LinkedIn
enter_username = wait.until(EC.presence_of_element_located((By.ID, 'username')))
enter_username.send_keys('deedadey@gmail.com')
enter_password = driver.find_element(By.ID, 'password')
enter_password.send_keys('Dee.Christ')
sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()

#
apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button--top-card')
apply_button.click()

next_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
next_button.click()
time.sleep(20)
