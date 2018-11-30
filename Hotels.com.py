
# coding: utf-8

# In[39]:


url = 'https://www.hotels.com/search.do?resolved-location=CITY%3A504261%3AUNKNOWN%3AUNKNOWN&destination-id=504261&q-destination=Paris,%20France&q-check-in=2019-02-14&q-check-out=2019-02-21&q-rooms=1&q-room-0-adults=2&q-room-0-children=0'
url


# In[40]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# In[41]:


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(r"C:\Users\shixinyue\Desktop\Columbia University\Tools for Analytics\web crawler\chromedriver")
driver.get(url)
driver.implicitly_wait(10)


# In[42]:


names = driver.find_elements_by_class_name('p-name')
for name in names:
    print(name.text)


# In[43]:


addresses = driver.find_elements_by_class_name('p-adr')
for address in addresses:
    print(address.text)


# In[46]:


prices = driver.find_elements_by_class_name('price')
for price in prices:
    print(price.text)


# In[47]:


reviews = driver.find_elements_by_class_name('guest-reviews')
for review in reviews:
    print(review.text)


# In[48]:


driver.refresh()
links=driver.find_elements_by_xpath("//a[contains(@href,'flex-link')]")
hotel_urls=list()
for link in links:
    hotel_urls.append(link.get_attribute('href'))
print(hotel_urls)

