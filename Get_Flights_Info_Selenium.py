
# coding: utf-8

# In[191]:


import requests
from bs4 import BeautifulSoup


# In[257]:


Departure='NYC'
Destination='PAR'
adult_num='1'
child_num='0'
dep_date='2019-02-14'
arr_date='2019-02-21'
#url= "https://www.airbnb.com/s/"+destination+"/homes?adults="+adult_num+"&children="+child_num+"&checkin="+cktin_date+"&checkout="+cktout_date+"&refinement_paths%5B%5D=%2"+"Fhomes&allow_override%5B%5D=&s_tag=Vobyce0e"
url= 'https://www.hipmunk.com/flights#f='+Departure+';t='+Destination+';d='+dep_date+';r='+arr_date+';is_search_for_business=false'
url


# In[258]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

import time
chrome_options = Options()
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(executable_path = '/Users/xiaohanliu/Desktop/Columbia/PYTHON/project/chromedriver')
driver.get(url)
driver.implicitly_wait(10)


# In[259]:


for _ in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# print all of the page source that was loaded
print(driver.page_source.encode("utf-8"))


# In[260]:


#Output Hotel: (name, address, zip code, rating, room_type, beds, people, price)
times=driver.find_elements_by_class_name('flight-tab-routing-info-popup__routing-times')
for name in names:
    print(name.text)

