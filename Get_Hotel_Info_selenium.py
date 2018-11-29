
# coding: utf-8

# In[1]:

get_ipython().system('pip install selenium')


# In[1]:

destination ='Paris--France'
adult_num='1'
child_num='0'
cktin_date='2019-02-14'
cktout_date='2019-02-21'
url= "https://www.airbnb.com/s/"+destination+"/homes?adults="+adult_num+"&children="+child_num+"&checkin="+cktin_date+"&checkout="+cktout_date+"&refinement_paths%5B%5D=%2"+"Fhomes&allow_override%5B%5D=&s_tag=Vobyce0e"
url


# In[2]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# In[8]:

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('/Users/zhangmingshan/Desktop/2018 Autumn/Tools for Analytics/Project/chromedriver')
driver.get(url)
driver.implicitly_wait(10)


# In[13]:

for _ in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# print all of the page source that was loaded
print(driver.page_source.encode("utf-8"))


# In[29]:

#Output Hotel: (name, address, zip code, rating, room_type, beds, people, price)
names=driver.find_elements_by_class_name('_2izxxhr')
for name in names:
    print(name.text)


# In[31]:

prices=driver.find_elements_by_class_name('_p1g77r')
for price in prices:
    print(price.text)


# In[32]:

descriptions=driver.find_elements_by_class_name('_1nhodd4u')
for description in descriptions:
    print(description.text)


# In[21]:

driver.refresh()
links=driver.find_elements_by_xpath("//a[contains(@href,'rooms')]")
hotel_urls=list()
for link in links:
    hotel_urls.append(link.get_attribute('href'))


# In[23]:

hotel_urls


# In[ ]:

###inside each url

