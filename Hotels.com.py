
# coding: utf-8

# In[39]:


city = 'Paris'
cktin = '2019-02-14'
cktout = '2019-02-21'
rooms = '1'
adults = '2'
children = '0'
url = "https://www.hotels.com/search.do?3A504261%3AUNKNOWN%3AUNKNOWN&q-destination="+city+"&q-check-in="+cktin+"&q-check-out="+cktout+"&q-rooms="+rooms+"&q-room-0-adults="+adults+"&q-room-0-children="+children+""
url


# In[40]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
import pandas as pd

# In[41]:


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(r"C:\Users\shixinyue\Desktop\Columbia University\Tools for Analytics\web crawler\chromedriver")
driver.get(url)
driver.implicitly_wait(10)


# In[42]:
hotel_list = []
hotels = driver.find_elements_by_class_name('hotel')
hotels_sponsored = driver.find_elemnets_by_class_name('hotel.sponsored')
hotels_vip = driver.find_elements_by_class_name('hotel.vip')
for hotel in hotels:
    name = hotel.find_elements_by_class_name('p-name')[0].text
    address = hotel.find_elements_by_class_name('p-adr')[0].text
    #price = hotel.find_elements_by_tag_name('ins')[0].text, stil have some bugs
    review = hotel.find_elements_by_class_name('guest-reviews')[0].text
    link = hotel.find_elements_by_tag_name('a')[0].get_attribute('href')
    hotel_list.append((name,address,review,link,#price))
                      
for hotel_sponsored in hotels_sponsored:

for hotel_vip in hotels_vip:                       

#old version codes as follows
                       
names = driver.find_elements_by_class_name('p-name')
for name in names:
    print(name.text)

addresses = driver.find_elements_by_class_name('p-adr')
for address in addresses:
    print(address.text)

prices = driver.find_elements_by_class_name('price')
for price in prices:
    print(price.text)

reviews = driver.find_elements_by_class_name('guest-reviews')
for review in reviews:
    print(review.text)

