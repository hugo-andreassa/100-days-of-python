from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

SITE_URL = "https://www.python.org/"

chrome_driver_path = "C:/Users/Hugo/Documents/GitHub/Outros/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get(SITE_URL)
date_list = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li/time")
name_list = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li/a")

events_dict = {}

for index in range(len(date_list)):
    events_dict[index] = {
        "date": date_list[index].text,
        "name": name_list[index].text
    }

pprint(events_dict)

driver.quit()
