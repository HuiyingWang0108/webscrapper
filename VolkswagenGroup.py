from dataclasses import is_dataclass
from msilib.schema import tables
from sqlite3 import Row
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Create an URL object
url = 'https://en.wikipedia.org/wiki/List_of_Volkswagen_Group_factories'

# Create object response
response = requests.get(url)

# parser-lxml = Change html to Python friendly format
# Obtain page's information
# soup = BeautifulSoup(res.text, 'lxml')
soup = BeautifulSoup(response.content, 'html.parser')


# the first argument to find tells it what tag to search for
# the second you can pass a dict of attr->value pairs to filter
# results that match the first tag
# table1 = soup.find('table', {"class":"wikitable sortable jquery-tablesorter"})
table = soup.find(class_="wikitable sortable jquery-tablesorter")
print(table)

# Obtain every title of columns with tag <th>
headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)
    print(title)

# Convert wrapped text in column 13 into one line text
# headers[3] = 'Tests/1M pop'

# Create a dataframe
mydata = pd.DataFrame(columns = headers)

# Create a for loop to fill mydata
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

# #
# raw_data = []
# raw_len = 0
# init = True
# # Create a for loop to fill mydata
# for j in table1.find_all('tr')[1:]:
#     row_data = j.find_all('td')
#     row = [i.text for i in row_data]
#     if init:
#         raw_len = len(row)
#         init = False
#     i = 0
#     while len(row) != raw_len:
#         row.insert(i, raw_data[-1][i])
#         i += 1
#     raw_data.append(row)
# print(raw_data)
# i = 0
# for data in raw_data:
#     print(len(data))
#     mydata.loc[i] = data
#     i += 1

# Export to csv
mydata.to_csv('Volkswagen_Group.csv', index=False)
# Try to read csv
mydata2 = pd.read_csv('Volkswagen_Group.csv')