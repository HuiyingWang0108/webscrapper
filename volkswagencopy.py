from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


url = 'https://www.volkswagenag.com/en/group/portrait-and-production-plants.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
elem = soup.select("#mapData1")
print(elem[0]["data-map"])
data_map = elem[0]["data-map"]
print(type(data_map))
# convert string to json object list
list_object = json.loads(data_map)

map_data_list = []

for obj_dict in list_object:
    map_dic = {}
    map_dic["PlantName"] = obj_dict["tooltip"]["name"]

    source_code = obj_dict["tooltip"]["copytext"]
    soup = BeautifulSoup(source_code, features="lxml")
    map_dic["Products"] = soup.find("p", {"class": "singlecolumntext"}).text.replace(
        "Products:", "").replace("\n", "")

    map_dic["mappath"] = obj_dict["mappath"].replace("worldwide:", "")
    map_dic["subline"] = obj_dict["tooltip"]["subline"].replace("<br>", " ")
    map_dic["latitude"] = obj_dict["lat"]
    map_dic["longitude"] = obj_dict["lon"]
    map_data_list.append(map_dic)

# Convert Json object of list to a string
json_str = json.dumps(map_data_list)
print(type(json_str))
df = pd.read_json(json_str)
df.to_csv("volkswagen0415.csv")
