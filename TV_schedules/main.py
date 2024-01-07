import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_browser = 'C:\Development\chromedriver.exe'

driver = selenium.webdriver.Chrome(service=Service(executable_path=chrome_browser))

joy_news_url = 'https://www.myjoyonline.com/media/joy-news-live/'

driver.get(joy_news_url)


table = driver.find_element(by=By.TAG_NAME, value='tbody')

monday01 = table.find_element(by=By.CSS_SELECTOR, value='tr td').text

print(monday01)


# import requests
# from bs4 import BeautifulSoup
#
# joy_news_response = requests.get(url='https://www.myjoyonline.com/media/joy-news-live/')
#
# joy_news_schedule = BeautifulSoup(joy_news_response.text, 'html.parser')
# # print(joy_news_schedule)
# td_elements = joy_news_schedule.find_all(name='td')
#
# programs = []
# times = []
#
# # for p_tag in td_elements:
# #     p_tag.find_all('p')
#
# # print(td_elements)
#
# oml = '<td>AM SHOW (Live)<p>5:00am - 7:00am</p></td>'
# print(oml.find('p'))
#
# # for td in td_elements:
# #     td_text = td.get_text(strip=True)
# #     p_element = td.find('p')
# #     p_text = p_element.get_text(strip=True)
# #     programs.append(td_text)
# #     times.append(p_text)
#
# print(programs)
# # print(times)
#
# for html in td_elements:
#     # Create a BeautifulSoup object for each item
#     soup = BeautifulSoup(html, 'html.parser')
#
#     # Find the <td> tag
#     td_tag = html.find('td')
#
#     # Check if a <td> tag was found
#     if td_tag:
#         # Remove text within <p> tags
#         for p_tag in td_tag.find_all('p'):
#             p_tag.extract()
#
#         # Get the cleaned text within <td> tag
#         cleaned_text = td_tag.get_text(strip=True)
#
#         # Append the cleaned text to the list
#         programs.append(cleaned_text)
#     else:
#         programs.append("No <td> tag found")
#
# print(programs)
