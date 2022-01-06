from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime, time

# GLOBAL CONSTANT
CHROME_DRIVER_PATH = Service("/Users/rodrigocamila/PycharmProjects/chromedriver")
HOUR_TO_STOP = "21:00"

# INFORMATION ABOUT TIME, INTERVAL BETWEEN CHECKS AND SCRIPT CLOSING
hour = datetime.datetime.now()
formatted_hour = datetime.datetime.strftime(hour, "%H:%M")
gap_to_check = datetime.timedelta(minutes=20)
timeout = hour + gap_to_check

# MAIN SCRIPT
while formatted_hour < HOUR_TO_STOP:
    if datetime.datetime.now() > timeout:
        driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
        driver.get(url="https://www.remessaonline.com.br/")
        driver.maximize_window()
        time.sleep(3)
        cotacao = driver.find_element(By.CSS_SELECTOR, "div.amount")
        print(cotacao.text)
        time.sleep(5)
        driver.quit()
        timeout += gap_to_check
        print(timeout)

# TODO Criar lista de cotações para cada dia e alerta para determinado valor ou percentual