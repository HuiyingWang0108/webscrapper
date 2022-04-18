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


url = 'https://corporate.ford.com/operations/locations/global-plants.html'
s = Service(r"C:\Users\v-huiywang\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(url)

# Locate the control.
elem = driver.find_element(by=By.CLASS_NAME, value="worldwide-locations-comp")
data_map = elem.get_attribute("data-worldwide-locations")
# convert string to json object list
list_object = json.loads(data_map)
# print(len(list_object))

# convert data format as you want
map_data_list = []
for obj_dict in list_object:
    map_dic = {}
    map_dic["PlantName"] = obj_dict["plantName"]
    map_dic["Products"] = obj_dict["currentProducts"]
    map_dic["mappath"] = obj_dict["country"]
    map_dic["numberOfEmployees"] = obj_dict["numberOfEmployees"]
    map_dic["yearOpened"] = obj_dict["yearOpened"]
    map_dic["plantSizeSquareFeet"] = obj_dict["plantSizeSquareFeet"]
    map_dic["siteSizeAcres"] = obj_dict["siteSizeAcres"]
    map_dic["yearOpened"] = obj_dict["yearOpened"]
    map_dic["state"] = obj_dict["state"]
    map_dic["city"] = obj_dict["city"]
    map_dic["address3"] = obj_dict["address3"]
    map_dic["address2"] = obj_dict["address2"]
    map_dic["address1"] = obj_dict["address1"]
    map_data_list.append(map_dic)

# Convert Json object of list to a string
json_str = json.dumps(map_data_list)
print(type(json_str))
df = pd.read_json(json_str)
df.to_csv("ford0415.csv")
