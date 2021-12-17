from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pprint import pprint

SITE_URL = "https://orteil.dashnet.org/cookieclicker/"

chrome_driver_path = "C:/Users/Hugo/Documents/GitHub/Outros/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get(SITE_URL)
article_count = driver.find_element(By.ID, "bigCookie")

while True:
    article_count.click()

# driver.quit()
