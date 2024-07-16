from selenium import webdriver
from selenium.webdriver.chrome.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

import time
import pickle
import os

from data import login, password


url = 'https://vk.com/'
service = EdgeService("D:\\MyProgramm\\SelenFox\\msedgedriver.exe")
path_cookies = f'cookies\\{login}_cookies.pkl'
ua = UserAgent()

edge_options = webdriver.EdgeOptions()
edge_options .add_argument(f'user-agent={ua.random}')

driver = webdriver.Edge(
    service=service,
    options=edge_options
)

try:
    driver.maximize_window()
    driver.get(url=url)
    time.sleep(5)

    if os.path.exists(path_cookies):
        for cookie in pickle.load(open(path_cookies, 'rb')):
            driver.add_cookie(cookie)

        time.sleep(5)
        driver.refresh()

    else:
        email_input = driver.find_element(By.ID, 'index_email')
        email_input.clear()
        email_input.send_keys(login)
        email_input.send_keys(Keys.ENTER)

        time.sleep(3)
        password_input = driver.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)
        cookies = driver.get_cookies()
        with open(path_cookies, 'wb') as file:
            pickle.dump(cookies, file)

    time.sleep(20)
    news_link = driver.find_element(By.ID, 'l_pr')
    news_link.click()
    time.sleep(20)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()