from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime, time

# GLOBAL CONSTANT
CHROME_DRIVER_PATH = Service("/Users/rodrigocamila/PycharmProjects/chromedriver")
HOUR_TO_STOP = "16:10"
GAP_TO_CHECK = datetime.timedelta(minutes=2)

# TIME TO CHECK
check_time = datetime.datetime.now() + GAP_TO_CHECK

currency_quote = {}

# MAIN SCRIPT
while True:
    hour = datetime.datetime.now()
    formatted_hour = datetime.datetime.strftime(hour, "%H:%M")
    if formatted_hour > HOUR_TO_STOP:
        break
    if datetime.datetime.now() > check_time:
        driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
        driver.get(url="https://www.remessaonline.com.br/")
        driver.maximize_window()
        time.sleep(3)
        cotacao = driver.find_element(By.CSS_SELECTOR, "div.amount")
        time.sleep(5)
        currency_quote[formatted_hour] = cotacao.text
        driver.quit()
        check_time += GAP_TO_CHECK
        print(currency_quote)

print(f"Finalizando programa e cotação fechou em {currency_quote.keys()}")

# TODO Criar lista de cotações para cada dia e alerta para determinado valor ou percentual