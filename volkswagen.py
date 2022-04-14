from operator import le
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


url = 'https://www.volkswagenag.com/en/group/portrait-and-production-plants.html'
s = Service(r"C:\Users\v-huiywang\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get(url) 

# Locate the control.
elem = driver.find_element(by = By.ID, value = "mapData1")
data_map = elem.get_attribute("data-map")
# convert string to json object list
list_object = json.loads(data_map)

map_data_list = []

for obj_dict in list_object:
    map_dic = {}
    map_dic["PlantName"] = obj_dict["tooltip"]["name"]

    source_code = obj_dict["tooltip"]["copytext"]
    soup = BeautifulSoup(source_code, features = "lxml")
    map_dic["Products"] = soup.find("p", {"class": "singlecolumntext"}).text.replace("Products:", "").replace("\n", "")

    map_dic["mappath"] = obj_dict["mappath"].replace("worldwide:", "")
    map_dic["subline"] = obj_dict["tooltip"]["subline"].replace("<br>", " ")
    map_data_list.append(map_dic)

# Convert Json object of list to a string
json_str = json.dumps(map_data_list)
print(type(json_str))
df = pd.read_json(json_str)
df.to_csv("volkswagen.csv")