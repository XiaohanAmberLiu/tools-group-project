
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
result = list()
hotels = driver.find_elements_by_class_name('info-and-price')
for hotel in hotels:
    link = hotel.find_elements_by_xpath("//a[@class='flex-link']")
    link.href
    #price = hotel.find_elements_by_class_name('actualPrice')[0].text
    #p = int(re.search(r'\d+',price).group())
    #if p <= budget:
    #name = hotel.find_elements_by_class_name('hotelTitle')[0].text
    #ratings = hotel.find_elements_by_class_name('starRating')
    #try:
        #rating = ratings[0].text
    #except:
        #pass
    #rates = hotel.find_elements_by_class_name('reviewOverall')
    #try:
        #rating = rates[0].text
    #except:
        #pass
 #reviews = hotel.find_elements_by_class_name('reviewCount')
        #review = reviews[1].text
        #for x in review:
            #temp = re.match(r'\d+',x.text)
            #if temp:
                #rev=temp.group()
            #link = hotel.find_elements_by_xpath("//a[@class='flex-link']")[0].get_attribute('href')

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


