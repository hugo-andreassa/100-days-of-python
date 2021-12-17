import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

EMAIL = "hugo.andreassa@gmail.com"
PASSWORD = "paquitoekiara12"
SITE_LINK = "https://www.linkedin.com/jobs/search/?f_LF=f_AL" \
            "&geoId=105871508&keywords=Desenvolvedor%20para%20iOS&location=S%C3%A3o%20Paulo%2C%20Brasil"
CHROME_DRIVER_PATH = "C:/Users/Hugo/Documents/GitHub/Outros/chromedriver.exe"

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))

driver.get(SITE_LINK)

entrar_btn = driver.find_element(By.CSS_SELECTOR, 'a.nav__button-secondary')
entrar_btn.click()

time.sleep(5)

username_input = driver.find_element(By.CSS_SELECTOR, 'input#username')
username_input.send_keys(EMAIL)

password_input = driver.find_element(By.CSS_SELECTOR, 'input#password')
password_input.send_keys(PASSWORD)

entrar_btn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
entrar_btn.click()

time.sleep(10)

job_cards = driver.find_elements(By.XPATH, '/html/body/div[6]/div[3]/div[3]/div[2]/'
                                           'div/section[1]/div/div/ul/li/div/div/div[1]/div[2]/div[1]')

print([item.text for item in job_cards])

# elements = driver.find_elements(By.CLASS_NAME, 'job-card-container')
# print(elements)
# print([element.text for element in elements])

# driver.quit()
