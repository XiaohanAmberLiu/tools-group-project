
# coding: utf-8

# In[49]:


url = 'https://www.trip.com/hotels/list?city=192&checkin=02-14-2019&checkout=02-21-2019&optionId=192&optionType=Intlcity&display=Paris%2C%20Ile-De-France%2C%20France&adult=1&children=0&ages=&label=LzdP1uB0N06XFxqjKHHdVg#ctm_ref=ix_sb_dl'
url


# In[50]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# In[51]:


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(r"C:\Users\shixinyue\Desktop\Columbia University\Tools for Analytics\web crawler\chromedriver")
driver.get(url)
driver.implicitly_wait(10)


# In[53]:


names = driver.find_elements_by_class_name('hotel-name')
for name in names:
    print(name.text)


# In[57]:


addresses = driver.find_elements_by_class_name('hotel-lm')
for address in addresses:
    print(address.text)


# In[59]:


prices = driver.find_elements_by_class_name('c-price')
for price in prices:
    print(price.text)


# In[58]:


reviews = driver.find_elements_by_class_name('hotel-review')
for review in reviews:
    print(review.text)


# In[48]:


driver.refresh()
links=driver.find_elements_by_xpath("//a[contains(@href,'flex-link')]")
hotel_urls=list()
for link in links:
    hotel_urls.append(link.get_attribute('href'))
print(hotel_urls)

