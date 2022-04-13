import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import os

# print(dir(selenium))

# url of the page we want to scrape
url = "https://global.toyota/en/company/profile/facilities/manufacturing-worldwide/"
# initiating the webdriver. Parameter includes the path of the webdriver.
s = Service(r"C:\Users\v-huiywang\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service = s)
print(type(driver))
driver.get(url) 

list_url = []
# Locate the control.
buttons = driver.find_elements(by = By.CLASS_NAME, value = "btn_text")
for btn in buttons:
    list_url.append(btn.get_attribute("href"))
for url in list_url:
    driver.get(url)
    res = requests.get(url)
    if res.status_code != 200:
        print("Error fetching page")
        exit()
    else:
        try:
            soup = BeautifulSoup(res.text, 'html.parser')
            table = soup.select('.newsTBL')
            # table = soup.select('#mw-content-text > div.mw-parser-output > table:nth-child(7)')
            df = pd.read_html(str(table))

            # convert list to dataframe
            df = pd.DataFrame(df[0])
            # print(df.head())
            # Export to csv
            os.makedirs("toyota", exist_ok=True)
            df.to_csv("toyota/{0}_toyota.csv".format(url.split("/")[-1].replace(".html", "")), index = False)
        except ValueError as err:
            print(url + " returned error: {0}".format(err))
