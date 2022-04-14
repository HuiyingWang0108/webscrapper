from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

class AutoManufactories:

    def __init__(self, url):
        self.url = url
    def scrape(self):
        print("the url is {0}".format(self.url))
        # initiating the webdriver. Parameter includes the path of the webdriver.
        s = Service(r"C:\Users\v-huiywang\webdriver\chromedriver.exe")
        driver = webdriver.Chrome(service = s)
        print(type(driver))
        driver.get(self.url) 
        buttons = driver.find_elements(by = By.CLASS_NAME, value = "btn_text")
        list_url = []
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
                    df = pd.read_html(str(table))
                    # convert list to dataframe
                    df = pd.DataFrame(df[0])
                    # Export to csv
                    os.makedirs("test", exist_ok = True)
                    df.to_csv("test/{0}_toyota.csv".format(url.split("/")[-1].replace(".html", "")), index = False)
                except ValueError as err:
                    print(url + " returned error: {0}".format(err))
            # driver.back()

obj = AutoManufactories("https://global.toyota/en/company/profile/facilities/manufacturing-worldwide/")
obj.scrape()