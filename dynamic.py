from traceback import print_tb
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
  
#url of the page we want to scrape
url = "https://www.volkswagenag.com/en/group/portrait-and-production-plants.html"
# Request URL: https://www.volkswagenag.com/content/dam/online-kommunikation/brands/corporate/world/presence/konzern/images/locations/europe/Schweden%20-%20Oskarshamn%20-%20Scania.jpg
# Request URL: https://www.volkswagenag.com/content/dam/online-kommunikation/brands/corporate/world/presence/konzern/images/locations/asia/Taiwan%20-%20Ping%20Chen%20City%20-%20Scania.jpg
# Request URL: https://www.volkswagenag.com/content/dam/online-kommunikation/brands/corporate/world/presence/konzern/images/locations/asia/Thailand%20-%20Amphur%20Pluakdaeng%20Rayong%20-%20Ducati.jpg
# Request URL: https://www.volkswagenag.com/content/dam/online-kommunikation/brands/corporate/world/presence/konzern/images/locations/northamerica/Tulsa-Navistar.jpg
# Request URL: https://www.volkswagenag.com/content/dam/online-kommunikation/brands/corporate/world/presence/konzern/images/locations/northamerica/USA%20-%20Chattanooga%20-%20VW.jpg
# Request URL: https://www.volkswagenag.com/content/dam/online-kommunikation/brands/corporate/world/presence/konzern/images/locations/northamerica/Springfield-Navistar.jpg

# Request URL: https://www.volkswagenag.com/content/dam/online-kommunikation/brands/corporate/world/presence/konzern/images/locations/northamerica/Mexiko%20-%20Puebla%20-%20VW.jpg
# Request URL: https://www.volkswagenag.com/content/dam/online-kommunikation/brands/corporate/world/presence/konzern/images/locations/northamerica/Mexiko%20-%20Puebla%20-%20VW.jpg

  
# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome(r'C:\Users\v-huiywang\webdriver\chromedriver') 
driver.get(url) 
  
# this is just to ensure that the page is loaded
time.sleep(5) 
  
html = driver.page_source
  
# this renders the JS code and stores all
# of the information in static HTML code.
  
# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('div', {'id' : 'map-container-v1-overlay'})
# all_divs = soup.select('#map-container-v1-overlay')
# print(all_divs)
plant_names = all_divs.find_all("h4", {"class": "js-maps-headline"})

for plant_name in plant_names:
    name = plant_name.text
    print(name)
# # printing top ten job profiles
# count = 0
# for job_profile in job_profiles :
#     print(job_profile.text)
#     count = count + 1
#     if(count == 10) :
#         break
  
# driver.close() # closing the webdriver