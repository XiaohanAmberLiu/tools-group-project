
# coding: utf-8

# In[34]:


import json
import requests
from bs4 import BeautifulSoup
from lxml import html


# In[166]:


# Setup Input
passenger_info = ['New York','United States of America','NYC','Paris','France','PAR','02-14-2019','02-21-2019',400,1]
trip = 'oneway'
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
print (departure,arrival,depart_country,arrival_country,depart_code,arrival_code,start_time,end_time,budget,people)


# In[167]:


################ First search Expedia ##################

########### Depart flight
url_expedia = 'https://www.expedia.com/Flights-Search?trip=oneway&leg1=from%3A'+departure+'%20('+depart_code+'-All%20Airports)%2Cto%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cdeparture%3A'+start_time[0]+'%2F'+start_time[1]+'%2F'+start_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com'

# This is the original url:
# url_expedia = 'https://www.expedia.com/Flights-Search?trip=oneway&leg1=from%3ANew%20York%20(NYC-All%20Airports)%2Cto%3AParis%2C%20France%20(PAR-All%20Airports)
# %2Cdeparture%3A02%2F14%2F2019TANYT&
# passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&
# options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com'


# In[168]:


response_expedia = requests.get(url_expedia)
# response_expedia.content


# In[176]:


results_page_expedia = BeautifulSoup(response_expedia.content,"html.parser")
#print(results_page_expedia.prettify())


# In[126]:


flight_list_expedia = results_page_expedia.find_all('li',{'class':'flight-module segment offer-listing '})


# In[127]:


len(flight_list_expedia)#.find('button').get('data-trip-id')
#.find('div',{'data-test-id':"flight-info"}).get_text().split()
#.find('div',{'class':'secondary-content no-wrap'}).find_all('span')


# In[133]:


# Get ticket info from Expedia
all_flight_expedia = []

for i in flight_list_expedia:
    price = i.find('h3').get_text()
    price = float(price[price.find('$')+1:])
    if price <= int(budget):
        depart_time = i.find('span',{'data-test-id':"departure-time"}).get_text()
        arrival_time = i.find('span',{'data-test-id':"arrival-time"}).get_text()
        #stop = i.find('span',{'data-test-num-stops':"arrival-time"}).get_text()
        airline = i.find('div',{'data-test-id':"airline-name"}).get_text().strip()
        depart_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[2]
        arrival_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[-1]
        #link = 'https://www.expedia.com/Flight-Information?offerToken=' + i.find('button').get('data-trip-id')
        link = url_expedia
        flight = (depart_airport,arrival_airport,depart_time,arrival_time,price,link)
        all_flight_expedia.append(flight)
    


# In[134]:


all_flight_expedia


# In[173]:


########## Now find return flight
url_expedia_re = 'https://www.expedia.com/Flights-Search?trip=oneway&leg1=from%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cto%3A'+departure+'%20('+departure_code+'-All%20Airports)%2Cdeparture%3A'+end_time[0]+'%2F'+end_time[1]+'%2F'+end_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com'


# In[174]:


# url_expedia_re1 = 'https://www.expedia.com/Flights-Search?trip=oneway&\
# leg1=from%3AParis%2C%20France%20(PAR-All%20Airports)%2Cto%3ANew%20York%20(NYC-All%20Airports)\
# %2Cdeparture%3A02%2F21%2F2019TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&\
# options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com'
# url_expedia_re == url_expedia_re1


# In[162]:


response_expedia_re = requests.get(url_expedia_re)
results_page_expedia_re = BeautifulSoup(response_expedia_re.content,"html.parser")
flight_list_expedia_re = results_page_expedia_re.find_all('li',{'class':'flight-module segment offer-listing '})


# In[163]:


####### Get return ticket info 
all_flight_expedia_re = []

for i in flight_list_expedia_re:
    price = i.find('h3').get_text()
    price = float(price[price.find('$')+1:])
    if price <= int(budget):
        depart_time = i.find('span',{'data-test-id':"departure-time"}).get_text()
        arrival_time = i.find('span',{'data-test-id':"arrival-time"}).get_text()
        #stop = i.find('span',{'data-test-num-stops':"arrival-time"}).get_text()
        airline = i.find('div',{'data-test-id':"airline-name"}).get_text().strip()
        depart_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[2]
        arrival_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[-1]
        #link = 'https://www.expedia.com/Flight-Information?offerToken=' + i.find('button').get('data-trip-id')
        link = url_expedia_re
        flight = (depart_airport,arrival_airport,depart_time,arrival_time,price,link)
        all_flight_expedia_re.append(flight)   


# In[164]:


all_flight_expedia_re


# In[135]:


##################### Search Hotwire ###################

###### depart flight
url_hotwire = 'https://vacation.hotwire.com/Flights-Search?tmid=21580175849&trip=OneWay&leg1=from:NYC,to:CDG,departure:02/14/2019TANYT&passengers=children:0,adults:1,seniors:0,infantinlap:Y&options=sortby:price&mode=search&paandi=true'
response_hotwire = requests.get(url_hotwire)
response_hotwire.status_code


# In[170]:


url_hotwire = 'https://vacation.hotwire.com/Flights-Search?trip=oneway&leg1=from%3A'+departure+'%2C%20'+depart_country+'%20('+depart_code+')%2Cto%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cdeparture%3A'+start_time[0]+'%2F'+start_time[1]+'%2F'+start_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=vacation.hotwire.com'


# In[175]:


# Original Url
# url_hotwire1 = 'https://vacation.hotwire.com/Flights-Search?trip=oneway&\
# leg1=from%3ANew%20York%2C%20United%20States%20of%20America%20(NYC)%2Cto%3AParis%2C%20France%20(PAR-All%20Airports)\
# %2Cdeparture%3A02%2F14%2F2019TANYT\
# &passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&\
# options=cabinclass%3Aeconomy&mode=search&origref=vacation.hotwire.com'
# print(url_hotwire)
# print(url_hotwire1)
# url_hotwire==url_hotwire1


# In[177]:


results_page_hotwire = BeautifulSoup(response_hotwire.content,'lxml')
#print(results_page_hotwire.prettify())


# In[156]:


flight_list_hotwire = results_page_hotwire.find_all('li',{'class':'flight-module segment offer-listing '})
#len(flight_list_hotwire)#[2].find_all('span')[6].get('data-test-num-stops')


# In[157]:


# Get depart flight info on Hotwire
all_flight_hotwire = []

for i in flight_list_hotwire:
    price = i.find('h3').get_text()
    price = float(price[price.find('$')+1:])
    if price <= int(budget):
        depart_time = i.find('span',{'data-test-id':"departure-time"}).get_text()
        arrival_time = i.find('span',{'data-test-id':"arrival-time"}).get_text()
        stop = i.find_all('span')[6].get('data-test-num-stops')
        airline = i.find('div',{'data-test-id':"airline-name"}).get_text().strip()
        depart_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[2]
        arrival_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[-1]
        # continuing websites on Hotwire is kind of random, so here we return search link.
        link = url_hotwire
        flight = (airline,depart_airport,arrival_airport,depart_time,arrival_time,stop,price,link)
        all_flight_hotwire.append(flight)    


# In[158]:


all_flight_hotwire

