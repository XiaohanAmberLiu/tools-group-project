
# coding: utf-8

# In[1]:


Departure='NYC'
Destination='PAR'
adult_num='1'
child_num='0'
dep_date='2019-02-14'
arr_date='2019-02-21'
#url= "https://www.airbnb.com/s/"+destination+"/homes?adults="+adult_num+"&children="+child_num+"&checkin="+cktin_date+"&checkout="+cktout_date+"&refinement_paths%5B%5D=%2"+"Fhomes&allow_override%5B%5D=&s_tag=Vobyce0e"
url= 'https://www.hipmunk.com/flights#f='+Departure+';t='+Destination+';d='+dep_date+';r='+arr_date+';is_search_for_business=false'
url


# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import re
import time
chrome_options = Options()
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(executable_path = '/Users/xiaohanliu/Desktop/Columbia/PYTHON/project/chromedriver')
driver.get(url)
driver.implicitly_wait(10)


# In[ ]:


for _ in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# print all of the page source that was loaded
print(driver.page_source.encode("utf-8"))


# In[ ]:


times=driver.find_elements_by_class_name('flight-tab-routing-info-popup__routing-times')
t=times[0].text
print(t)

for name in times:
    temp=name.text.split('–')
    print([temp[0],temp[1]])


# In[ ]:



airports=driver.find_elements_by_class_name('FlightRowMiddleColumn__airports')
airport_name=list()
for name in airports:
    airport_name.append(name.find_elements_by_tag_name('span'))

#print(airport_name)

print(len(airport_name))

departure_airport=list()
arrival_airport=list()
i=0
temp_airport=list()
while i < len(airport_name):
    departure_airport.append(airport_name[0:3])
    arrival_airport.append(airport_name[3:6])
    temp_airport.append(airport_name)
    i+=1

departure_airport[0][0].text
arrival_airport


# In[ ]:


price=driver.find_elements_by_class_name('FlightPrice')
price_number=list()
for name in price:
    price_number.append(name.find_elements_by_tag_name('div'))

print(len(price_number))
i=0
temp_price=list()
while i < len(price_number):
    temp_price.append(price_number[i][0].text)
    i+=1
temp_price

if temp<=budget:
    price=temp_price
    
    


# In[ ]:


flight=(price,)


# In[ ]:


#driver.refresh()
#links=driver.find_elements_by_xpath(".//*[(@class_='FlightResultsListItem')]")

flight_urls=list()
for link in links:
    flight_urls.append(link.get_attribute('href'))
    


# In[18]:


flight_list_priceline=driver.find_elements_by_xpath("//div[@class='FlightResultsListItem FlightRowDesktop']")
#print(flight_list_priceline)


for i in flight_list_priceline:
    price=i.find_element_by_class_name('FlightPrice').text
    price_number = int(re.findall("\d+",price)[0])
    print(price_number)
    
    if price_number<= 700:
    #assume a budget
        airports=i.find_elements_by_class_name('FlightRowMiddleColumn__airports')[0].text
        print(airports)
        times=i.find_elements_by_class_name('flight-tab-routing-info-popup__routing-times')[0].text
        print(times)
        split_times=times.split('–')
        print(split_times)
        departure_time=split_times[0]
        print(departure_time)
        arrival_time=split_times[1]
        print(arrival_time)


# In[16]:


flight_list_priceline=driver.find_elements_by_xpath("//div[@class='FlightResultsListItem FlightRowDesktop']")
flight_list_priceline

