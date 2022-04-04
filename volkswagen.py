import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.volkswagenag.com/en/group/portrait-and-production-plants.html'
response = requests.get(url)
if response.status_code != 200:
    print("Error fetching page")
    exit()
else:
    content = response.content

# parse data from the html into a beautifulsoup object
# soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(response.content, 'html.parser')
page_data = soup.select('#section_510890826 > div.maps.abstractContentComponent.parbase.section > div > div')
print(page_data.prettify)

# df = pd.read_html(str(table))
# # convert list to dataframe
# df = pd.DataFrame(df[0])
# print(df.head())

# # drop the unwanted columns
# df.drop(columns=['PlantVIN IDcode(s)', 'Formervehicleproduction', 'Number ofemployees', 'Plantcoordinates'])
# # rename the column name
# df.rename(columns={"Location(continent,country)": "country", "Location(town / city,state / region)": "location"})

# # Export to csv
# df.to_csv('test.csv', index=False)