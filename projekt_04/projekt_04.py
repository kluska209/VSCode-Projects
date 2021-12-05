from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import argparse
from rich.console import Console
import rich.traceback
import os
import json
import time

parser = argparse.ArgumentParser()
parser.add_argument('name', help = 'name of file to return')
args = parser.parse_args()

console = Console()
console.clear()
rich.traceback.install()

options = Options()
options.add_argument('--disable-notifications')

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service = service, options = options)

try:
    driver.get("https://www.onet.pl/")
except TimeoutException:
    console.print('Błąd połączenia.')
else:
    try:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageMainContainer"]/div[9]/div[1]/div[2]/div/div[6]/button[2]')))
        button.click()

        link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'WIADOMOŚCI')))
        link.click()

        for i in range(5):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)

        articles1 = driver.find_elements(By.CLASS_NAME, 'title')
        list1 = [{'Artykół': article.text} for article in articles1]
        console.print(list1)

        with open(os.getcwd()+f'\\{args.name}', mode='w', encoding='utf-8') as file:
            json.dump(list1, file, indent=2)

    except NoSuchElementException:
        console.print('Błąd połączenia.')
    except TimeoutException:
        console.print('Błąd połączenia.')



    
