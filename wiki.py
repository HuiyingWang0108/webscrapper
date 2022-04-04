import requests
from bs4 import BeautifulSoup
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/List_of_Volkswagen_Group_factories'
# wiki_url = 'https://en.wikipedia.org/wiki/List_of_Toyota_factories'
response = requests.get(wiki_url)
if response.status_code != 200:
    print("Error fetching page")
    exit()
else:
    content = response.content
# print(content)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.select('#mw-content-text > div.mw-parser-output > table:nth-child(12)')
# table = soup.select('#mw-content-text > div.mw-parser-output > table:nth-child(7)')
df = pd.read_html(str(table))

# convert list to dataframe
df = pd.DataFrame(df[0])

# drop the unwanted columns
data = df.drop(["PlantVIN IDcode(s)","Formervehicleproduction","Number ofemployees","Plantcoordinates"], axis=1)
# data = df.drop(["Unit production[needs update]","Operator.1","Operator", "Employees[needs update]"], axis=1)
# rename the column name
data = data.rename(columns={"Location(continent,country)": "country", "Location(town / city,state / region)": "location"})

# Export to csv
data.to_csv('wiki.csv', index = False)
# data.to_csv('toyota.csv', index = False)