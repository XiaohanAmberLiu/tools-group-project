


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

