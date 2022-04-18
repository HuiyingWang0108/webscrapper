import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.carlogos.org/reviews/largest-car-companies.html'
# response = requests.get(url)
response = requests.get(url, headers={"User-Agent": "XY"})

if response.status_code != 200:
    print(response.status_code)
    print("Error fetching page")
    exit()
else:
    content = response.content

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.select('body > div.article > div.review-content > table')
df = pd.read_html(str(table))

# convert list to dataframe
df = pd.DataFrame(df[0])

# drop the unwanted columns
# data = df.drop(["PlantVIN IDcode(s)","Formervehicleproduction","Number ofemployees","Plantcoordinates"], axis=1)
# rename the column name
# data = data.rename(columns={"Location(continent,country)": "country", "Location(town / city,state / region)": "location"})

# Export to csv
df.to_csv('topGlobalAutoManufactoriesSuppliers.csv', index = False)