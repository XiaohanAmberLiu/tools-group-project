
# coding: utf-8

# In[1]:


Departure='NYC'
Destination='PAR'
adult_num='1'
child_num='0'
dep_date='2019-02-14'
arr_date='2019-02-21'
url_re= 'https://www.hipmunk.com/flights#f='+Departure+';t='+Destination+';d='+dep_date+';r='+arr_date+';is_search_for_business=false;group=1'
url_re


# In[6]:


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
driver_re=webdriver.Chrome(executable_path = '/Users/xiaohanliu/Desktop/Columbia/PYTHON/project/chromedriver')
driver_re.get(url_re)
driver_re.implicitly_wait(10)


# In[7]:


for _ in range(100):
    driver_re.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# print all of the page source that was loaded
print(driver_re.page_source.encode("utf-8"))


# In[15]:


flight_list_priceline_re=driver_re.find_elements_by_xpath("//div[@class='FlightResultsListItem FlightRowDesktop']")
print(flight_list_priceline_re)
all_flight_priceline_re=[]

for i in flight_list_priceline_re:
    price_number_re=i.find_element_by_class_name('FlightPrice').text
    price_re =int(re.findall("\d+",price_number_re)[0])
    print(price_re)
    
    if price_re<= 700:
    #assume a budget
        airports_re=i.find_elements_by_class_name('FlightRowMiddleColumn__airports')[0].text
        print(airports_re)
        split_airports_re=airports_re.split(' → ')
        depart_airport_re = str(split_airports_re[0])
        print(depart_airport_re)
        arrival_airport_re = str(split_airports_re[1])
        print(arrival_airport_re)
        times_re=i.find_elements_by_class_name('flight-tab-routing-info-popup__routing-times')[0].text
        print(times_re)
        split_times_re=times_re.split('–')
        print(split_times_re)
        depart_time_re=str(split_times_re[0])
        print(depart_time_re)
        arrival_time_re=str(split_times_re[1])
        print(arrival_time_re)
        airline_re=i.find_elements_by_class_name('FlightRowLeftColumn__airline-name')[0].text
        stop_re='NA'
        link_re=url_re
        flight=(airline_re,depart_airport_re,arrival_airport_re,depart_time_re,arrival_time_re,stop_re,price_re,link_re)
        all_flight_priceline_re.append(flight)

print(all_flight_priceline_re)


