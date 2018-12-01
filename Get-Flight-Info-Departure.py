
# coding: utf-8

# In[ ]:


Departure='NYC'
Destination='PAR'
adult_num='1'
child_num='0'
dep_date='2019-02-14'
arr_date='2019-02-21'
#url= "https://www.airbnb.com/s/"+destination+"/homes?adults="+adult_num+"&children="+child_num+"&checkin="+cktin_date+"&checkout="+cktout_date+"&refinement_paths%5B%5D=%2"+"Fhomes&allow_override%5B%5D=&s_tag=Vobyce0e"
url= 'https://www.hipmunk.com/flights#f='+Departure+';t='+Destination+';d='+dep_date+';r='+arr_date+';is_search_for_business=false'
url


# In[ ]:


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


flight_list_priceline=driver.find_elements_by_xpath("//div[@class='FlightResultsListItem FlightRowDesktop']")
#print(flight_list_priceline)
all_flight_priceline=[]


for i in flight_list_priceline:
    price_number=i.find_element_by_class_name('FlightPrice').text
    price =int(re.findall("\d+",price_number)[0])
    print(price)
    
    if price<= 700:
    #assume a budget
        airports=i.find_elements_by_class_name('FlightRowMiddleColumn__airports')[0].text
        print(airports)
        split_airports=airports.split(' → ')
        depart_airport = str(split_airports[0])
        print(depart_airport)
        arrival_airport = str(split_airports[1])
        print(arrival_airport)
        times=i.find_elements_by_class_name('flight-tab-routing-info-popup__routing-times')[0].text
        print(times)
        split_times=times.split('–')
        print(split_times)
        depart_time=str(split_times[0])
        print(departure_time)
        arrival_time=str(split_times[1])
        print(arrival_time)
        airline=i.find_elements_by_class_name('FlightRowLeftColumn__airline-name')[0].text
        print(airline)
        stop='NA'
        link=url
        flight=(airline,depart_airport,arrival_airport,depart_time,arrival_time,stop,price,link)
        all_flight_priceline.append(flight)

print(all_flight_priceline)

