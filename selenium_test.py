from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver_path = r"C:\Users\danil\Documents\scrapping\webdriver\chromedriver.exe"
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/explore/tags/naturabroficial/")

time.sleep(5)

get_element = browser.find_element(By.TAG_NAME, "link")

print(get_element.text)

browser.close()