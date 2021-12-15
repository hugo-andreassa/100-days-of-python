from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pprint import pprint

SITE_URL = "https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal"

chrome_driver_path = "C:/Users/Hugo/Documents/GitHub/Outros/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
