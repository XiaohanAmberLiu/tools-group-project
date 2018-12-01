
# coding: utf-8

# In[1]:


city = 'Paris'
cktin_year = '2019'
cktin_month = '02'
cktin_day = '14'
cktout_year = '2019'
cktout_month = '02'
cktout_day = '21'
rooms = '1'
adults = '2'
children = '0'
url = "https://www.expedia.com/Hotel-Search?destination="+city+"&startDate="+cktin_month+"%2F"+cktin_day+"%2F"+cktin_year+"&endDate="+cktout_month+"%2F"+cktout_day+"%2F"+cktout_year+"&rooms="+rooms+"&adults="+adults+""
url


# In[2]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
import pandas as pd

# In[3]:


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(r"C:\Users\shixinyue\Desktop\Columbia University\Tools for Analytics\web crawler\chromedriver")
driver.get(url)
driver.implicitly_wait(10)


# In[5]:


names = driver.find_elements_by_class_name('hotelTitle')
for name in names:
    print(name.text)


# In[6]:


reviews = driver.find_elements_by_class_name('reviewOverall')
for review in reviews:
    print(review.text)


# In[7]:


prices = driver.find_elements_by_class_name('actualPrice')
for price in prices:
    print(price.text)


