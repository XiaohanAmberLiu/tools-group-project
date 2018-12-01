
# coding: utf-8

# In[ ]:


### We picked up 5 flight websites and 4 hotel websites, and did some web scraping on these website.
### The main steps are:
### 1. Input user information including departure city, destination, travel duration, budget and number of travellers.
### 2. Get qualified flight info from Expedia, Hotwire, Priceline and Hipmunk.
### 3. Get qualified hotel info from Airbnb, Booking and XXXXXX.
### 4. Combine flight and hotel info then filter to generater travel packages.
### 5. Sort the packages by price, rating and recommendation.


# In[4]:


from selenium import webdriver
import json
import requests
from bs4 import BeautifulSoup
from lxml import html


# In[31]:


########## STEP 1 Input user information ##########
passenger_info = ['New York','United States of America','NYC','Paris','France','PAR','02-14-2019','02-21-2019',3000,1,0]

people = str(passenger_info[9])
children = str(passenger_info[10])
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


# In[6]:


########## STEP 2 Get Flight Info ##########

# Get Flight Info on Expedia
# Depart flight
url_expedia = 'https://www.expedia.com/Flights-Search?trip=oneway&leg1=from%3A'+departure+'%20('+depart_code+'-All%20Airports)%2Cto%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cdeparture%3A'+start_time[0]+'%2F'+start_time[1]+'%2F'+start_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com'

response_expedia = requests.get(url_expedia)
results_page_expedia = BeautifulSoup(response_expedia.content,"html.parser")
flight_list_expedia = results_page_expedia.find_all('li',{'class':'flight-module segment offer-listing '})

all_flight_expedia = []
for i in flight_list_expedia:
    price = i.find('h3').get_text()
    price = float(price[price.find('$')+1:])
    if price <= int(budget):
        depart_time = i.find('span',{'data-test-id':"departure-time"}).get_text()
        arrival_time = i.find('span',{'data-test-id':"arrival-time"}).get_text()
        stop = i.find_all('span')[6].get('data-test-num-stops')
        airline = i.find('div',{'data-test-id':"airline-name"}).get_text().strip()
        depart_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[2]
        arrival_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[-1]
        #link = 'https://www.expedia.com/Flight-Information?offerToken=' + i.find('button').get('data-trip-id')
        link = url_expedia
        flight = (airline,depart_airport,arrival_airport,depart_time,arrival_time,stop,price,link)
        all_flight_expedia.append(flight)

all_flight_expedia


# In[7]:


# Now find return flight
url_expedia_re = 'https://www.expedia.com/Flights-Search?trip=oneway&leg1=from%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cto%3A'+departure+'%20('+depart_code+'-All%20Airports)%2Cdeparture%3A'+end_time[0]+'%2F'+end_time[1]+'%2F'+end_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com'

response_expedia_re = requests.get(url_expedia_re)
results_page_expedia_re = BeautifulSoup(response_expedia_re.content,"html.parser")
flight_list_expedia_re = results_page_expedia_re.find_all('li',{'class':'flight-module segment offer-listing '})

all_flight_expedia_re = []
for i in flight_list_expedia_re:
    price = i.find('h3').get_text()
    price = float(price[price.find('$')+1:])
    if price <= int(budget):
        depart_time = i.find('span',{'data-test-id':"departure-time"}).get_text()
        arrival_time = i.find('span',{'data-test-id':"arrival-time"}).get_text()
        stop = i.find_all('span')[4].get('data-test-num-stops')
        airline = i.find('div',{'data-test-id':"airline-name"}).get_text().strip()
        depart_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[2]
        arrival_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[-1]
        #link = 'https://www.expedia.com/Flight-Information?offerToken=' + i.find('button').get('data-trip-id')
        link = url_expedia_re
        flight = (airline,depart_airport,arrival_airport,depart_time,arrival_time,stop,price,link)
        all_flight_expedia_re.append(flight)   

all_flight_expedia_re


# In[8]:


# Get Flight Info on Hotwire
# depart flight
url_hotwire = 'https://vacation.hotwire.com/Flights-Search?trip=oneway&leg1=from%3A'+departure+'%2C%20'+depart_country+'%20('+depart_code+'-ALL%20Airports)%2Cto%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cdeparture%3A'+start_time[0]+'%2F'+start_time[1]+'%2F'+start_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=vacation.hotwire.com'

response_hotwire = requests.get(url_hotwire)
response_hotwire.status_code
results_page_hotwire = BeautifulSoup(response_hotwire.content,'lxml')
flight_list_hotwire = results_page_hotwire.find_all('li',{'class':'flight-module segment offer-listing '})

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

all_flight_hotwire


# In[9]:


# Now get the return flight info on Hotwire
url_hotwire_re = 'https://vacation.hotwire.com/Flights-Search?trip=oneway&leg1=from%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cto%3A'+departure+'%2C%20'+depart_country+'%20('+depart_code+'-All%20Airports)%2Cdeparture%3A'+end_time[0]+'%2F'+end_time[1]+'%2F'+end_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=vacation.hotwire.com'

response_hotwire_re = requests.get(url_hotwire_re)
#response_hotwire_re.status_code
results_page_hotwire_re = BeautifulSoup(response_hotwire_re.content,'lxml')
flight_list_hotwire_re = results_page_hotwire_re.find_all('li',{'class':'flight-module segment offer-listing '})

all_flight_hotwire_re = []
for i in flight_list_hotwire_re:
    price = i.find('h3').get_text()
    price = float(price[price.find('$')+1:])
    if price <= int(budget):
        depart_time = i.find('span',{'data-test-id':"departure-time"}).get_text()
        arrival_time = i.find('span',{'data-test-id':"arrival-time"}).get_text()
        stop = i.find_all('span')[4].get('data-test-num-stops')
        airline = i.find('div',{'data-test-id':"airline-name"}).get_text().strip()
        depart_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[2]
        arrival_airport = i.find('div',{'data-test-id':"flight-info"}).get_text().split()[-1]
        # continuing websites on Hotwire is kind of random, so here we return search link.
        link = url_hotwire_re
        flight = (airline,depart_airport,arrival_airport,depart_time,arrival_time,stop,price,link)
        all_flight_hotwire_re.append(flight)   
        
all_flight_hotwire_re


# In[10]:


# Get Flight Info on Priceline

# Generate flight search URL
url_priceline = 'https://www.priceline.com/m/fly/search/'+depart_code+'-'+arrival_code+'-'+start_time[2]+start_time[0]+start_time[1]+'/'+arrival_code+'-'+depart_code+'-'+end_time[2]+end_time[0]+end_time[1]+'/?cabin-class=ECO&no-date-search=false&search-type=1111&num-adults='+people

# Start Scraping
browser_priceline = webdriver.Chrome()
browser_priceline.get(url_priceline)
for _ in range(100):
    browser_priceline.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
flight_list_priceline = browser_priceline.find_elements_by_class_name('sc-jdfcpN')


# In[11]:


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

print(all_flight_priceline)
print(all_flight_priceline_re)
browser_priceline.close()


# In[ ]:


# Get Flight Info on Hipmunk


# In[12]:


########## STEP 3 Get Hotel Info ##########

# Get Hotel Info on Airbnb 
# Get URL on Airbnb
def get_main_url(destination,adult_num,child_num,cktin_date,cktout_date):
    url="https://www.airbnb.com/s/"+destination+"/homes?adults="+adult_num+"&children="+child_num+"&checkin="+cktin_date+"&checkout="+cktout_date+"&refinement_paths%5B%5D=%2"+"Fhomes&allow_override%5B%5D=&s_tag=Vobyce0e"
    return url


# In[28]:


# Get Page Info Function
def get_page_info(url,budget,page_total_num=1): 
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    import re
    import pandas as pd

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome()
    try:
        driver.get(url)
    except:
        return "Connection Failure"

    page=1
    result=list()
    while page<=page_total_num:
        driver.implicitly_wait(5)
        Hotels=driver.find_elements_by_class_name('_qlq27g')
        for Hotel in Hotels:
            #get hotel price in total
            try:
                Price=Hotel.find_elements_by_class_name('_p1g77r')
                pr=Price[0].text
                
                #delete the ',' in price
                pr=pr.replace(',','')
                    
                p=int(re.search(r'\d+',pr).group())
                if p<=budget:
                    #get hotel url
                    try:
                        link=Hotel.find_elements_by_tag_name('a')
                        l=link[0].get_attribute('href')
                    except:
                        l=""

                    #get hotel name
                    try:
                        name=Hotel.find_elements_by_class_name('_2izxxhr')
                        n=name[0].text
                    except:
                        n=""

                    #get hotel description
                    try:
                        Descrips=Hotel.find_elements_by_class_name('_1nhodd4u')
                        d=""
                        for Descrip in Descrips:
                            d += ' · ' + Descrip.text
                    except:
                        d=""

                    #rating
                    try:
                        rating=Hotel.find_elements_by_class_name('_q27mtmr')
                        ra=rating[0].find_elements_by_tag_name('span')
                        r=ra[0].get_attribute('aria-label')
                    except:
                        r=""

                    ##num of reviews
                    try:
                        review=Hotels[0].find_elements_by_class_name('_1m8bb6v')
                        for x in review:
                            temp=re.match(r'\d+',x.text)
                            if temp:
                                rev=temp.group()
                    except:
                        rev=""

                    result.append((n,p,r,rev,d,l))
                else:
                    continue
                
            except:
                continue
                  
        page += 1  
        driver.find_element_by_class_name('_1rltvky').click()
        driver.refresh()
    driver.close()
                                
    return result


# In[29]:


# Combination Function
def get_airbnb_list(destination,adult_num,child_num,cktin_date,cktout_date,budget):
    url=get_main_url(destination,adult_num,child_num,cktin_date,cktout_date)
    #print(url)
    return get_page_info(url,budget,page_total_num=1)


# In[32]:


# Now get the results on Airbnb
hotel_airbnb = get_airbnb_list(arrival,people,children,start_time[2]+'-'+start_time[0]+'-'+start_time[1],end_time[2]+'-'+end_time[0]+'-'+end_time[1],int(budget))
# Output format:(name,total_price,rating,# of comments,description,link)
hotel_airbnb


# In[45]:


len(hotel_airbnb)


# In[37]:


########## STEP 4 Combine and Filter ##########

# Combine all flight info (except Priceline)
def get_all_depart_flight():
    flight_list = []
    all_flight = []
    # First combine all flights
    all_flight.extend(all_flight_expedia)
    all_flight.extend(all_flight_hotwire)
    # For the same flights, keep the cheaper one.
    for i in all_flight:
        same = False
        for j in flight_list:
            if j[0]==i[0] and j[1]==i[1] and j[2]==i[2] and j[3]==i[3] and j[4]==i[4]:
                same = True
                if i[6]<j[6]:
                    flight_list.remove(j)
                    flight_list.append(i)
                    break
                else:
                    break
        if same == False:
            flight_list.append(i)
    return flight_list
            
def get_all_return_flight():
    flight_list = []
    all_flight = []
    # First combine all flights
    all_flight.extend(all_flight_expedia_re)
    all_flight.extend(all_flight_hotwire_re)
    # For the same flights, keep the cheaper one.
    for i in all_flight:
        same = False
        for j in flight_list:
            if j[0]==i[0] and j[1]==i[1] and j[2]==i[2] and j[3]==i[3] and j[4]==i[4]:
                same = True
                if i[6]<j[6]:
                    flight_list.remove(j)
                    flight_list.append(i)
                    break
                else:
                    break
        if same == False:
            flight_list.append(i)
    return flight_list


# In[38]:


# Combine all hotel info
def get_all_hotels():
    hotel_list = []
    all_hotel = []
    all_hotel.extend(hotel_airbnb)
    
    for i in all_hotel:
        same = False
        for j in hotel_list:
            if j[0]==i[0]:
                same = True
                if i[1]<j[1]:
                    hotel_list.remove(j)
                    hotel_list.append(i)
                    break
                else:
                    break
        if same == False:
            hotel_list.append(i)
    return hotel_list


# In[61]:


# Combine flights and hotels, then generate qualified packages.
def possible_package(departflights,returnflights,hotels):
    packages = []
    for i in departflights:
        for j in returnflights:
            for h in hotels:
                package_price = i[6]+j[6]+h[1]
                if package_price<=float(budget):
                    packages.append(list(i)+list(j)+list(h)+[package_price])
    return packages

# Priceline only offer total, so we generate a special function for Priceline
def priceline_package(departflights,returnflights,hotels):
    packages = []
    for i in range(len(departflights)):
            for h in hotels:
                package_price = float(departflights[i][6])+float(returnflights[i][6])+h[1]
                if package_price<=float(budget):
                    packages.append(list(departflights[i])+list(returnflights[i])+list(h)+[package_price])
    return packages


# In[62]:


all_packages = possible_package(get_all_depart_flight(),get_all_return_flight(),
                                get_all_hotels()) + priceline_package(all_flight_priceline,all_flight_priceline_re,get_all_hotels())


# In[63]:


print(len(all_packages))
#all_packages
import pandas as pd
import numpy as np
columns = ['depart airline','depart airport1','depart airport2','depart flight depart time','depart flight arrival time',
          'depart flight stops','depart flight price','depart flight link',
           'arrival airline','arrival airport1','arrival airport2','arrival flight depart time','arrival flight arrival time',
          'arrival flight stops','arrival flight price','arrival flight link',
           'hotel name','hotel price','rating','comments','description','hotel link','total package price']
df_packages = pd.DataFrame(all_packages,columns=columns)
df_packages

