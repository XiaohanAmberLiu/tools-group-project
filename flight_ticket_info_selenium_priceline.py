
# coding: utf-8

# In[1]:


# Use Selenium Package
from selenium import webdriver

# Setup Input
passenger_info = ['New York','United States of America','NYC','Paris','France','PAR','02-14-2019','02-21-2019',400,1]

people = str(passenger_info[9])
budget = str(passenger_info[8])
departure = passenger_info[0].replace(' ','%20')
arrival = passenger_info[3].replace(' ','%20')
depart_country = passenger_info[1].replace(' ','%20')
arrival_country = passenger_info[4].replace(' ','%20')
depart_code = passenger_info[2]
arrival_code = passenger_info[5]
start_time = passenger_info[6].split('-')
end_time = passenger_info[7].split('-')
#print (departure,arrival,depart_country,arrival_country,depart_code,arrival_code,start_time,end_time,budget,people)

# Generate flight search URL
url_priceline = 'https://www.priceline.com/m/fly/search/'+depart_code+'-'+arrival_code+'-'+start_time[2]+start_time[0]+start_time[1]+'/'+arrival_code+'-'+depart_code+'-'+end_time[2]+end_time[0]+end_time[1]+'/?cabin-class=ECO&no-date-search=false&search-type=1111&num-adults='+people

# Originial URL
# url_priceline1 = 'https://www.priceline.com/m/fly/search/NYC-PAR-20190214\
# /PAR-NYC-20190221/?cabin-class=ECO&no-date-search=false&search-type=1111&num-adults=1'
# url_priceline ==url_priceline1


# In[2]:


# Get flight info on Priceline
browser = webdriver.Chrome()
browser.get(url_priceline)

for _ in range(100):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# print source code
# print(browser.page_source.encode("utf-8"))


# In[3]:


flight_list_priceline = browser.find_elements_by_class_name('sc-jdfcpN')
#flight_list_priceline[1]


# In[4]:


all_flight_priceline = []
all_flight_priceline_re = []

for i in flight_list_priceline:
    # Note that on Priceline, the price is the total price of the round-trip flight.
    price = i.find_elements_by_xpath(".//*[@data-test='rounded-dollars']")[0].text
    
    if price <= budget:
        depart_airport = i.find_elements_by_xpath(".//*[@data-test='left-airport-code']")[0].text
        arrival_airport = i.find_elements_by_xpath(".//*[@data-test='right-airport-code']")[0].text
        depart_airport_re = i.find_elements_by_xpath(".//*[@data-test='left-airport-code']")[1].text
        arrival_airport_re = i.find_elements_by_xpath(".//*[@data-test='right-airport-code']")[1].text
        depart_time = i.find_elements_by_tag_name('time')[0].text
        arrival_time = i.find_elements_by_tag_name('time')[1].text
        depart_time_re = i.find_elements_by_tag_name('time')[2].text
        arrival_time_re = i.find_elements_by_tag_name('time')[3].text
        airline = i.find_elements_by_class_name('sc-bFADNz')[0].text
        airline_re = i.find_elements_by_class_name('sc-bFADNz')[1].text
        stop = i.find_elements_by_xpath(".//*[@data-test='stops-text-component']")[0].text
        stop_re = i.find_elements_by_xpath(".//*[@data-test='stops-text-component']")[1].text
        link = url_priceline
        flight = (airline,depart_airport,arrival_airport,depart_time,arrival_time,stop,price,link)
        flight_re = (airline_re,depart_airport_re,arrival_airport_re,depart_time_re,arrival_time_re,stop_re,price,link)
        all_flight_priceline.append(flight)
        all_flight_priceline_re.append(flight_re)  


# In[5]:


print(len(all_flight_priceline))
print(len(all_flight_priceline_re))
print(all_flight_priceline)
print(all_flight_priceline_re)


# In[6]:


browser.close()

