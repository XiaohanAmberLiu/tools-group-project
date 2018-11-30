
# coding: utf-8

# In[ ]:

#!pip install selenium


# In[2]:

def get_main_url(destination,adult_num,child_num,cktin_date,cktout_date):
    url="https://www.airbnb.com/s/"+destination+"/homes?adults="+adult_num+"&children="+child_num+"&checkin="+cktin_date+"&checkout="+cktout_date+"&refinement_paths%5B%5D=%2"+"Fhomes&allow_override%5B%5D=&s_tag=Vobyce0e"
    return url


# In[3]:

url=get_main_url('Paris--France','1','0','2019-02-14','2019-02-21')
url


# In[4]:

def get_onepage_info(url):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    import re
    import pandas as pd


    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome('/Users/zhangmingshan/Desktop/2018 Autumn/Tools for Analytics/Project/chromedriver')
    driver.get(url)
    driver.implicitly_wait(10)
    #find all names
    names_list=list()
    names=driver.find_elements_by_class_name('_2izxxhr')
    for name in names:
        names_list.append(name.text)

    #find all prices
    prices_list=list()
    prices=driver.find_elements_by_class_name('_p1g77r')
    for price in prices: 
        p=re.search(r'\d+',price.text)
        prices_list.append(p.group())


    #find all descriptions
    descriptions_list=list()
    descriptions=driver.find_elements_by_class_name('_1nhodd4u')
    for description in descriptions:
        descriptions_list.append(description.text)

    #find urls
    hotel_urls=list()
    links=driver.find_elements_by_xpath("//a[contains(@href,'rooms')]")
    for link in links:
        hotel_urls.append(link.get_attribute('href'))
        
    #hotel_data = pd.DataFrame({'Name': names_list,'Prices_total': prices_list,'Description': descriptions_list,'Urls':hotel_urls})
    
    return (names_list,prices_list,descriptions_list,hotel_urls)


# In[5]:

a=get_onepage_info(url)


# In[6]:

a


# In[7]:

print(len(a[0]),len(a[1]),len(a[2]),len(a[3]))


# In[ ]:

for _ in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# print all of the page source that was loaded
print(driver.page_source.encode("utf-8"))


# In[ ]:

#Output Hotel: (name, address, zip code, rating, room_type, beds, people, price)
names=driver.find_elements_by_class_name('_2izxxhr')
for name in names:
    print(name.text)


# In[ ]:

import re
a='$123jiom'
match=re.search(r'^[$]',a)
bool(match)


# In[ ]:

import re
prices=driver.find_elements_by_class_name('_p1g77r')
for price in prices:
    print(re.search(r'\d+',price.text).group())


# In[ ]:

descriptions=driver.find_elements_by_class_name('_1nhodd4u')
for description in descriptions:
    print(description.text)


# In[ ]:

driver.refresh()
links=driver.find_elements_by_xpath("//a[contains(@href,'rooms')]")
hotel_urls=list()
for link in links:
    hotel_urls.append(link.get_attribute('href'))


# In[ ]:




# In[ ]:

hotel_urls


# In[ ]:

###inside each url

