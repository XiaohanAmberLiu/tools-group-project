
# coding: utf-8

# In[1]:


import json
import requests
from bs4 import BeautifulSoup
from lxml import html


# In[14]:


# First search Expedia
url_expedia = 'https://www.expedia.com/Flights-Search?trip=oneway&leg1=from%3ANew%20York%2C%20NY%2C%20United%20States%20(JFK)%2Cto%3AParis%2C%20France%20(PAR)%2Cdeparture%3A02%2F14%2F2019TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com'


# In[15]:


response_expedia = requests.get(url_expedia)
response_expedia.status_code


# In[16]:


results_page_expedia = BeautifulSoup(response_expedia.content,"html.parser")
#print(results_page.prettify())


# In[17]:


flight_list_expedia = results_page_expedia.find_all('li',{'class':'flight-module segment offer-listing '})


# In[18]:


flight_list_expedia[1]#.find('button').get('data-trip-id')
#.find('div',{'data-test-id':"flight-info"}).get_text().split()
#.find('div',{'class':'secondary-content no-wrap'}).find_all('span')


# In[19]:


# Get ticket info from Expedia
all_flight_expedia = []
budget = 370
for i in flight_list_expedia:
    price = i.find('h3').get_text()
    price = float(price[price.find('$')+1:])
    if price <= budget:
        depart_time = i.find('span',{'data-test-id':"departure-time"}).get_text()
        arrival_time = i.find('span',{'data-test-id':"arrival-time"}).get_text()
        #stop = i.find('span',{'data-test-num-stops':"arrival-time"}).get_text()
        airline = i.find('div',{'data-test-id':"airline-name"}).get_text().strip()
        depart_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[2]
        arrival_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[-1]
        link = 'https://www.expedia.com/Flight-Information?offerToken=' + i.find('button').get('data-trip-id')
        flight = (depart_airport,arrival_airport,depart_time,arrival_time,price,link)
        all_flight_expedia.append(flight)
    


# In[20]:


all_flight_expedia

