
# coding: utf-8

# In[1]:


url = 'https://www.expedia.com/Hotel-Search?destination=Paris,+France&startDate=02/14/2019&endDate=02/21/2019&adults=1&regionId=179898&latLong=48.86272,2.34375'
url


# In[2]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


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


# In[8]:


driver.refresh()
links=driver.find_elements_by_xpath("//a[contains(@href,'flex-link')]")
hotel_urls=list()
for link in links:
    hotel_urls.append(link.get_attribute('href'))
print(hotel_urls)

