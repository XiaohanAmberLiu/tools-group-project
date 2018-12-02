
# coding: utf-8

# In[ ]:


### We picked up 5 flight websites and 2 hotel websites, and did some web scraping on these website.
### The main steps are:
### 1. Input user information including departure city, destination, travel duration, budget and number of travellers.
### 2. Get qualified flight info from Expedia, Hotwire, Priceline and Hipmunk.
### 3. Get qualified hotel info from Airbnb and Booking.
### 4. Combine flight and hotel info then filter to generater travel packages.
### 5. Sort the packages by price, rating and recommendation.


# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import re
import time
import json
import requests
from bs4 import BeautifulSoup
from lxml import html


# In[41]:


########## STEP 1 Input user information ##########

# INPUT HAS BEEN MOVED TO THE END, RIGHT BEFORE THE 'generate_packages()' FUNCTION.

# passenger_info = ['New York','United States of America','NYC','Paris','France','PAR','02-14-2019','02-21-2019',3000,1,0]

# people = str(passenger_info[9])
# children = str(passenger_info[10])
# budget = passenger_info[8]
# departure = passenger_info[0].replace(' ','%20')
# arrival = passenger_info[3].replace(' ','%20')
# depart_country = passenger_info[1].replace(' ','%20')
# arrival_country = passenger_info[4].replace(' ','%20')
# depart_code = passenger_info[2]
# arrival_code = passenger_info[5]
# start_time = passenger_info[6].split('-')
# end_time = passenger_info[7].split('-')

# print (departure,arrival,depart_country,arrival_country,depart_code,arrival_code,start_time,end_time,budget,people)


# In[5]:


########## STEP 2 Get Flight Info ##########

# Get Flight Info on Expedia
# Depart flight
def get_flight_expedia(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget):
    
    url_expedia = 'https://www.expedia.com/Flights-Search?trip=oneway&leg1=from%3A'+departure+'%20('+depart_code+'-All%20Airports)%2Cto%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cdeparture%3A'+start_time[0]+'%2F'+start_time[1]+'%2F'+start_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com'
#     print(url_expedia)
#     print(url_expedia=='https://www.expedia.com/Flights-Search?trip=oneway&leg1=from%3ANew%20York%20(NYC-All%20Airports)%2Cto%3AParis%2C%20France%20(PAR-All%20Airports)%2Cdeparture%3A02%2F14%2F2019TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com')
    response_expedia = requests.get(url_expedia)
    results_page_expedia = BeautifulSoup(response_expedia.content,"html.parser")
    flight_list_expedia = results_page_expedia.find_all('li',{'class':'flight-module segment offer-listing '})

    all_flight_expedia = []
    for i in flight_list_expedia:
        price = i.find('h3').get_text()
        price = float(price[price.find('$')+1:])
        if float(price) <= budget:
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

    return all_flight_expedia


# In[6]:


# all_flight_expedia = get_flight_expedia(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget)
# all_flight_expedia


# In[7]:


# Now find return flight
def get_flight_expedia_re(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget):
    url_expedia_re = 'https://www.expedia.com/Flights-Search?trip=oneway&leg1=from%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cto%3A'+departure+'%20('+depart_code+'-All%20Airports)%2Cdeparture%3A'+end_time[0]+'%2F'+end_time[1]+'%2F'+end_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com'

    response_expedia_re = requests.get(url_expedia_re)
    results_page_expedia_re = BeautifulSoup(response_expedia_re.content,"html.parser")
    flight_list_expedia_re = results_page_expedia_re.find_all('li',{'class':'flight-module segment offer-listing '})

    all_flight_expedia_re = []
    for i in flight_list_expedia_re:
        price = i.find('h3').get_text()
        price = float(price[price.find('$')+1:])
        if float(price) <= budget:
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

    return all_flight_expedia_re


# In[8]:


# all_flight_expedia_re = get_flight_expedia_re(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget)
# all_flight_expedia_re


# In[9]:


# Get Flight Info on Hotwire
# depart flight
def get_flight_hotwire(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget):

    url_hotwire = 'https://vacation.hotwire.com/Flights-Search?trip=oneway&leg1=from%3A'+departure+'%2C%20'+depart_country+'%20('+depart_code+'-ALL%20Airports)%2Cto%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cdeparture%3A'+start_time[0]+'%2F'+start_time[1]+'%2F'+start_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=vacation.hotwire.com'

    response_hotwire = requests.get(url_hotwire)
    response_hotwire.status_code
    results_page_hotwire = BeautifulSoup(response_hotwire.content,'lxml')
    flight_list_hotwire = results_page_hotwire.find_all('li',{'class':'flight-module segment offer-listing '})

    all_flight_hotwire = []
    for i in flight_list_hotwire:
        price = i.find('h3').get_text()
        price = float(price[price.find('$')+1:])
        if float(price) <= budget:
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

    return all_flight_hotwire


# In[10]:


# all_flight_hotwire = get_flight_hotwire(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget)
# all_flight_hotwire


# In[11]:


# Now get the return flight info on Hotwire
def get_flight_hotwire_re(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget):

    url_hotwire_re = 'https://vacation.hotwire.com/Flights-Search?trip=oneway&leg1=from%3A'+arrival+'%2C%20'+arrival_country+'%20('+arrival_code+'-All%20Airports)%2Cto%3A'+departure+'%2C%20'+depart_country+'%20('+depart_code+'-All%20Airports)%2Cdeparture%3A'+end_time[0]+'%2F'+end_time[1]+'%2F'+end_time[2]+'TANYT&passengers=adults%3A'+people+'%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=vacation.hotwire.com'

    response_hotwire_re = requests.get(url_hotwire_re)
    #response_hotwire_re.status_code
    results_page_hotwire_re = BeautifulSoup(response_hotwire_re.content,'lxml')
    flight_list_hotwire_re = results_page_hotwire_re.find_all('li',{'class':'flight-module segment offer-listing '})

    all_flight_hotwire_re = []
    for i in flight_list_hotwire_re:
        price = i.find('h3').get_text()
        price = float(price[price.find('$')+1:])
        if float(price) <= budget:
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

    return all_flight_hotwire_re


# In[12]:


# all_flight_hotwire_re = get_flight_hotwire_re(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget)
# all_flight_hotwire_re


# In[13]:


# Get Flight Info on Priceline

# Generate flight search URL
def get_flight_priceline(arrival_code,depart_code,start_time,end_time,people,budget):
    url_priceline = 'https://www.priceline.com/m/fly/search/'+depart_code+'-'+arrival_code+'-'+start_time[2]+start_time[0]+start_time[1]+'/'+arrival_code+'-'+depart_code+'-'+end_time[2]+end_time[0]+end_time[1]+'/?cabin-class=ECO&no-date-search=false&search-type=1111&num-adults='+people
    #print(url_priceline)
    # Start Scraping
    browser_priceline = webdriver.Chrome()
    browser_priceline.get(url_priceline)
    for _ in range(100):
        browser_priceline.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    flight_list_priceline = browser_priceline.find_elements_by_class_name('sc-jdfcpN')
    #print(flight_list_priceline)
    all_flight_priceline = []
    all_flight_priceline_re = []

    for i in flight_list_priceline:
        # Note that on Priceline, the price is the total price of the round-trip flight.
        price = i.find_element_by_xpath(".//*[@data-test='rounded-dollars']").text

#         try:
#             price = i.find_element_by_xpath(".//*[@data-test='rounded-dollars']")[0].text
#         except:
#             break
#             ('Robot Check! Please try again later.')

        if float(price) <= budget:
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

#     print(all_flight_priceline)
#     print(all_flight_priceline_re)
    browser_priceline.close()
    if all_flight_priceline ==[]:
        raise ValueError('Robot Check! Please try again later.')
        
    return all_flight_priceline,all_flight_priceline_re


# In[14]:


# all_flight_priceline,all_flight_priceline_re = get_flight_priceline(arrival_code,depart_code,start_time,end_time,people,budget)


# In[15]:


# Get Flight Info on Hipmunk

#  Hipmunk URL
def get_flight_hipmunk(departure,arrival,start_time,end_time):
    url= 'https://www.hipmunk.com/flights#f='+departure+';t='+arrival+';d='+start_time[2]+'-'+start_time[0]+'-'+start_time[1]+';r='+end_time[2]+'-'+end_time[0]+'-'+end_time[1]+';is_search_for_business=false'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver=webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)

    for _ in range(100):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    flight_list= driver.find_elements_by_xpath("//div[@class='FlightResultsListItem FlightRowDesktop']")
    #print(flight_list_priceline)
    all_flight=[]
    #print(len(flight_list))
    for i in flight_list:
        try:
            price_number=i.find_element_by_class_name('FlightPrice').text
            price =int(re.findall("\d+",price_number)[0])
        except:
            price = 9999999999999999999
        if price<= budget:
            airports=i.find_elements_by_class_name('FlightRowMiddleColumn__airports')[0].text
            split_airports=airports.split(' → ')
            depart_airport = str(split_airports[0])
            arrival_airport = str(split_airports[1])
            times=i.find_elements_by_class_name('flight-tab-routing-info-popup__routing-times')[0].text
            split_times=times.split('–')
            depart_time=str(split_times[0])
            arrival_time=str(split_times[1])
            airline=i.find_elements_by_class_name('FlightRowLeftColumn__airline-name')[0].text
            stop='NA'
            link=url
            flight=(airline,depart_airport,arrival_airport,depart_time,arrival_time,stop,price,link)
            all_flight.append(flight)
    driver.close()
    return all_flight


# In[16]:


# all_flight_hipmunk = get_flight_hipmunk(departure,arrival,start_time,end_time)
# all_flight_hipmunk


# In[17]:


def get_flight_hipmunk_re(departure,arrival,start_time,end_time):

    url_re= 'https://www.hipmunk.com/flights#f='+departure+';t='+arrival+';d='+start_time[2]+'-'+start_time[0]+'-'+start_time[1]+';r='+end_time[2]+'-'+end_time[0]+'-'+end_time[1]+';is_search_for_business=false;group=1'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver_re=webdriver.Chrome()
    driver_re.get(url_re)
    driver_re.implicitly_wait(10)
    for _ in range(100):
        driver_re.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    flight_list_priceline_re=driver_re.find_elements_by_xpath("//div[@class='FlightResultsListItem FlightRowDesktop']")
    all_flight_priceline_re=[]

    for i in flight_list_priceline_re:
        price_number_re=i.find_element_by_class_name('FlightPrice').text
        price_re =int(re.findall("\d+",price_number_re)[0])
    
        if price_re<= budget:
        #assume a budget
            airports_re=i.find_elements_by_class_name('FlightRowMiddleColumn__airports')[0].text
            split_airports_re=airports_re.split(' → ')
            depart_airport_re = str(split_airports_re[0])
            arrival_airport_re = str(split_airports_re[1])
            times_re=i.find_elements_by_class_name('flight-tab-routing-info-popup__routing-times')[0].text
            split_times_re=times_re.split('–')
            depart_time_re=str(split_times_re[0])
            arrival_time_re=str(split_times_re[1])
            airline_re=i.find_elements_by_class_name('FlightRowLeftColumn__airline-name')[0].text
            stop_re='NA'
            link_re=url_re
            flight=(airline_re,depart_airport_re,arrival_airport_re,depart_time_re,arrival_time_re,stop_re,price_re,link_re)
            all_flight_priceline_re.append(flight)
    driver_re.close()
    return all_flight_priceline_re


# In[18]:


# all_flight_hipmunk_re = get_flight_hipmunk_re(departure,arrival,start_time,end_time)
# all_flight_hipmunk_re


# In[19]:


########## STEP 3 Get Hotel Info ##########

# Get Hotel Info on Airbnb 
# Get URL on Airbnb
def get_main_url_airbnb(destination,adult_num,child_num,cktin_date,cktout_date):
    url="https://www.airbnb.com/s/"+destination+"/homes?adults="+adult_num+"&children="+child_num+"&checkin="+cktin_date+"&checkout="+cktout_date+"&refinement_paths%5B%5D=%2"+"Fhomes&allow_override%5B%5D=&s_tag=Vobyce0e"
    return url


# In[20]:


# Get Page Info Function
def get_page_info_airbnb(url,budget,page_total_num=1): 
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
                        review=Hotel.find_elements_by_class_name('_1m8bb6v')
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


# In[21]:


# Combination Function
def get_airbnb_list(destination,adult_num,child_num,cktin_date,cktout_date,budget):
    url=get_main_url_airbnb(destination,adult_num,child_num,cktin_date,cktout_date)
    #print(url)
    return get_page_info_airbnb(url,budget,page_total_num=1)


# In[22]:


# Now get the results on Airbnb
# hotel_airbnb = get_airbnb_list(arrival,people,children,start_time[2]+'-'+start_time[0]+'-'+start_time[1],end_time[2]+'-'+end_time[0]+'-'+end_time[1],int(budget))
# # Output format:(name,total_price,rating,# of comments,description,link)
# hotel_airbnb


# In[23]:


# Get Hotel Info on Booking 

# send basic info to booking
def set_basic_info_booking(destination,adult_num,child_num,cktin_date,cktout_date):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import Select
    import re
    import time

    
    url='https://www.booking.com/'
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome()
    try:
        driver.get(url)
    except:
        print("Connection Failure")
    driver.maximize_window()
    driver.implicitly_wait(15)
    
    #Set destination
    dest=driver.find_element_by_xpath("//input[@type='search']")
    dest.send_keys(destination)
    
    #open calender
    cals=driver.find_elements_by_xpath("//button[@aria-label='Open calendar']")
    cals[0].click()
    
    #format the checkin time
    cktin_date_format=time.strptime(cktin_date,"%Y-%m-%d")
    ckt_year=cktin_date_format.tm_year
    ckt_mon=cktin_date_format.tm_mon

    #find the calendar
    while True:
        cals=driver.find_elements_by_xpath("//div[@class='bui-calendar__month']")
        cal=cals[0].text
        cal_date_format=time.strptime(cal,"%B %Y")
        cal_year=cal_date_format.tm_year
        cal_mon=cal_date_format.tm_mon
        if (cal_year!=ckt_year) or (cal_mon!=ckt_mon):
            driver.find_element_by_xpath("//div[@data-bui-ref='calendar-next']").click()
        else:
            break
        
    start_dates=driver.find_elements_by_xpath("//td[@class='bui-calendar__date'][@data-bui-ref='calendar-date']")
    
    #click checkin date
    for start_date in start_dates:
        if cktin_date.strip() == start_date.get_attribute('data-date').strip():
            start_date.click()

    #click checkout date
    for start_date in start_dates:
        if cktout_date.strip() == start_date.get_attribute('data-date').strip():
            start_date.click()    
            

    person_button=driver.find_element_by_xpath("//label[@for='xp__guests__input']")
    person_button.click()

    #set people
    #person+button
    add_button=driver.find_elements_by_xpath("//button[@type='button'][@class='bui-button bui-button--secondary bui-stepper__add-button']")
    add_button=add_button[1:]

    #person-button
    sub_button=driver.find_elements_by_xpath("//button[@type='button'][@class='bui-button bui-button--secondary bui-stepper__subtract-button']")
    sub_button=sub_button[1:]


    while True:
        guests=driver.find_element_by_class_name("xp__guests__count").text
        adult_web=int(re.findall('\d+',guests)[0])
        child_web=int(re.findall('\d+',guests)[1])
        adult_num=int(adult_num)
        child_num=int(child_num)
    
        if (adult_web!=adult_num) or (child_web!=child_num):
            try:
                select_a = Select(driver.find_element_by_name('group_adults'))
                select_a.select_by_value(str(adult_num))
                select_c = Select(driver.find_element_by_name('group_children'))
                select_c.select_by_value(str(child_num))
                break
            except:
                if adult_web>adult_num:
                    sub_button[0].click()
                elif adult_web<adult_num:
                    add_button[0].click()

                if child_web>child_num:
                    sub_button[1].click()
                elif child_web<child_num:
                    add_button[1].click()      
        else:
            break
    
    #click submit
    submit=driver.find_element_by_xpath("//button[@type='submit'][@data-sb-id='main']")
    submit.click()
    
    return driver
        


# In[24]:


def get_page_info_booking(driver,budget,page_total_num=1):  
    import re
    from selenium import webdriver
    page=1
    result=list()
    while page<=page_total_num:
        driver.implicitly_wait(10)
        Hotels=driver.find_elements_by_xpath("//div[@class='sr_item_content sr_item_content_slider_wrapper ']")
        for Hotel in Hotels:
            #get hotel price in total
            try:
                Price=Hotel.find_elements_by_tag_name('strong')
                pr=Price[0].text

                #delete the ',' in price
                pr=pr.replace(',','')
                p=int(re.search(r'\d+',pr).group())

                if p<=budget:
                    #get hotel url
                    try:
                        link=Hotel.find_elements_by_xpath(".//a[@class='hotel_name_link url']")
                        l=link[0].get_attribute('href')
                    except:
                        l=""

                    #get hotel name
                    try:
                        name=Hotel.find_elements_by_class_name('sr-hotel__name')
                        n=name[0].text
                    except:
                        n=""

                    #get hotel description
                    try:
                        Descrips=Hotel.find_elements_by_class_name('room_link')
                        d=Descrips[0].text
                        d=d.replace('\n',' · ')
                    except:
                        d=""

                    #rating
                    try:
                        rating=Hotel.find_elements_by_class_name('bui-review-score__badge')
                        r=rating[0].text
                    except:
                        r=""

                    ##num of reviews
                    try:
                        review=Hotel.find_elements_by_class_name('bui-review-score__text')
                        rev=re.match(r'\d+',review[0].text.replace(',','')).group()

                    except:
                        rev=""

                    result.append((n,p,float(r)/10,rev,d,l))
                else:
                    continue

            except:
                pass

        page += 1  
        driver.find_element_by_xpath("//li[@class='bui-pagination__item bui-pagination__next-arrow']").click()
        driver.refresh()

    driver.close()
    return result


# In[25]:


def get_booking_list(destination,adult_num,child_num,cktin_date,cktout_date,budget):
    driver=set_basic_info_booking(destination,adult_num,child_num,cktin_date,cktout_date)
    return get_page_info_booking(driver,budget,page_total_num=1)


# In[26]:


# hotel_booking = get_booking_list('Paris',int(people),int(children),
#                                  start_time[2]+'-'+start_time[0]+'-'+start_time[1],
#                                  end_time[2]+'-'+end_time[0]+'-'+end_time[1],budget)
# hotel_booking


# In[95]:


########## STEP 4 Combine and Filter Hotels and Flights ##########

# Combine all flight info (except Priceline)
def get_all_depart_flight(all_flight_expedia,all_flight_hotwire,all_flight_hipmunk):
    flight_list = []
    all_flight = []
    # First combine all flights
    all_flight.extend(all_flight_expedia)
    all_flight.extend(all_flight_hotwire)
    all_flight.extend(all_flight_hipmunk)
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
            
def get_all_return_flight(all_flight_expedia_re,all_flight_hotwire_re,all_flight_hipmunk_re):
    flight_list_re = []
    all_flight_re = []
    # First combine all flights
    all_flight_re.extend(all_flight_expedia_re)
    all_flight_re.extend(all_flight_hotwire_re)
    all_flight_re.extend(all_flight_hipmunk_re)
    # For the same flights, keep the cheaper one.
    for i in all_flight_re:
        same = False
        for j in flight_list_re:
            if j[0]==i[0] and j[1]==i[1] and j[2]==i[2] and j[3]==i[3] and j[4]==i[4]:
                same = True
                if i[6]<j[6]:
                    flight_list_re.remove(j)
                    flight_list_re.append(i)
                    break
                else:
                    break
        if same == False:
            flight_list_re.append(i)
    return flight_list_re


# In[96]:


# Combine all hotel info
def get_all_hotels(hotel_airbnb,hotel_booking):
    hotel_list = []
    all_hotel = []
    all_hotel.extend(hotel_airbnb)
    all_hotel.extend(hotel_booking)
    
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


# In[97]:


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
                package_price = float(departflights[i][6])+h[1]
                if package_price<=float(budget):
                    packages.append(list(departflights[i])+list(returnflights[i])+list(h)+[package_price])
    return packages


# In[98]:


########## STEP 5 Sorting #########

# standardize hotel rating
def change_airbnb_rating(rat):
    import re
    if re.match(r'Rating',str(rat)):
        return (float(re.findall(r'\d',rat)[0])/float(re.findall(r'\d',rat)[1]))
    else:
        try:
            return (float(rat))
        except:
            return 'NaN'

#price normalization (max-x)/(max-min)
def normalization(df,m=1): #m=1=>(x-min)/(max-min); m=0 =>(max-x)/(max-min)
    mx=df.max()
    mn=df.min()
    if m==1:
        return df.apply(lambda x: (x-mn)/(mx-mn))
    else:
        return df.apply(lambda x: (mx-x)/(mx-mn))


# In[99]:


def generate_packages(passenger_info,sort = 0):
    people = str(passenger_info[9])
    children = str(passenger_info[10])
    budget = passenger_info[8]
    departure = passenger_info[0].replace(' ','%20')
    arrival = passenger_info[3].replace(' ','%20')
    depart_country = passenger_info[1].replace(' ','%20')
    arrival_country = passenger_info[4].replace(' ','%20')
    depart_code = passenger_info[2]
    arrival_code = passenger_info[5]
    start_time = passenger_info[6].split('-')
    end_time = passenger_info[7].split('-')
    
    all_flight_expedia = get_flight_expedia(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget)
    all_flight_expedia_re = get_flight_expedia_re(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget)
    all_flight_hotwire = get_flight_hotwire(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget)
    all_flight_hotwire_re = get_flight_hotwire_re(arrival,arrival_country,arrival_code,departure,depart_code,depart_country,start_time,end_time,people,budget)
    all_flight_priceline,all_flight_priceline_re = get_flight_priceline(arrival_code,depart_code,start_time,end_time,people,budget)
    all_flight_hipmunk = get_flight_hipmunk(departure,arrival,start_time,end_time)
    all_flight_hipmunk_re = get_flight_hipmunk_re(departure,arrival,start_time,end_time)
    hotel_airbnb = get_airbnb_list(arrival,people,children,start_time[2]+'-'+start_time[0]+'-'+start_time[1],end_time[2]+'-'+end_time[0]+'-'+end_time[1],budget)
    hotel_booking = get_booking_list(arrival,int(people),int(children),
                                     start_time[2]+'-'+start_time[0]+'-'+start_time[1],
                                     end_time[2]+'-'+end_time[0]+'-'+end_time[1],budget)
    all_packages = possible_package(get_all_depart_flight(all_flight_expedia,all_flight_hotwire,all_flight_hipmunk),
                                    get_all_return_flight(all_flight_expedia_re,all_flight_hotwire_re,all_flight_hipmunk_re),
                                    get_all_hotels(hotel_airbnb,hotel_booking)) + priceline_package(all_flight_priceline,all_flight_priceline_re,get_all_hotels(hotel_airbnb,hotel_booking))
#     except NameError:
#         print("There's something wrong with expedia.com. Please try agin after several minutes.")
              
    import pandas as pd
    import numpy as np
    columns = ['depart airline','depart airport1','depart airport2','depart flight depart time','depart flight arrival time',
              'depart flight stops','depart flight price','depart flight link',
               'arrival airline','arrival airport1','arrival airport2','arrival flight depart time','arrival flight arrival time',
              'arrival flight stops','arrival flight price','arrival flight link',
               'hotel name','hotel price','rating','comments','description','hotel link','total package price']
    df_packages = pd.DataFrame(all_packages,columns=columns)
    
    import re
    df_packages['comments']=pd.to_numeric(df_packages['comments']) 
    #normalizae rating
    df_packages['rating']=df_packages['rating'].apply(lambda x: change_airbnb_rating(x))
    
    if sort==0:
        #sort by package price, hotel rating 
        result=df_packages.sort_values(by=['total package price','rating'],ascending=[True,False])
    
    elif sort==1:
        #sort by hotel rating, price 
        result=df_packages.sort_values(by=['rating','total package price'],ascending=[False,True])

    elif sort==2:
        #recommendation score weight: price 50%, Rating 30%, comments 20%
        df_packages['std_pkg_price']= normalization(df_packages['total package price'],m=0)
        df_packages['std_comments']= normalization(df_packages['comments'],m=1)
        df_packages['recommend_score']=df_packages['std_pkg_price']*0.2  + df_packages['std_comments']*0.4+ df_packages['rating']*0.4
        result=df_packages.sort_values(by=['recommend_score'],ascending=False)
    
    else:
        print('Sorry, we can not recognize the sorting condition. Please try again.')
     
    print('This is all the qualified sorted packages. Please choose one from them.')
    return result
  


# In[100]:


###################### THIS IS THE INPUT #######################

# When using this tool, you could uncomment the following codes and input whatever you want.
# But pay attention to the format!!!

# passenger_info = [input('Plase input the departure city:'),input('Plase input the departure Country:'),input('Plase input the departure city code:'),
#                  input('Plase input the destination city:'),input('Plase input the destination country:'),
#                  input('Plase input the destination code:'),input('Plase input the depart date (MM-DD-YYYY):'),
#                  input('Plase input the return date (MM-DD-YYYY):'),int(input('Plase input a budget(int):')),
#                   int(input('Plase input the number of adults(int):')),int(input('Plase input the number of children(int):'))]

# sort = int(input('Please input the sorting method(0:by price,1:by rating,2:by recommendation):'))


# In[101]:


# For now, we take input as following for instance.
passenger_info = ['New York','United States of America','NYC','Paris','France','PAR','02-14-2019','02-21-2019',3000,1,0]
sort = 2


# In[102]:


results = generate_packages(passenger_info,sort)


# In[ ]:


df_backup = df_packages
df_packages
#len(df_packages)


# In[ ]:


df_packages =df_backup


# In[ ]:


def recommended_packages(df_packages,sort=2):  #0:sorted by total price; 1:sorted by hotel's rating; 2:sorted by recommendation
##data processing
    import pandas as pd
    import re
    df_packages['comments']=pd.to_numeric(df_packages['comments']) 
    #normalizae rating
    df_packages['rating']=df_packages['rating'].apply(lambda x: change_airbnb_rating(x))
    
    if sort==0:
        #sort by package price, hotel rating 
        result=df_packages.sort_values(by=['total package price','rating'],ascending=[True,False])
    
    elif sort==1:
        #sort by hotel rating, price 
        result=df_packages.sort_values(by=['rating','total package price'],ascending=[False,True])

    elif sort==2:
        #recommendation score weight: price 50%, Rating 30%, comments 20%
        df_packages['std_pkg_price']= normalization(df_packages['total package price'],m=0)
        df_packages['std_comments']= normalization(df_packages['comments'],m=1)
        df_packages['recommend_score']=df_packages['std_pkg_price']*0.2  + df_packages['std_comments']*0.4+ df_packages['rating']*0.4
        result=df_packages.sort_values(by=['recommend_score'],ascending=False)
    
    else:
        print('Sorry, we can not recognize the sorting condition. Please try again.')
    #print(result.info())
    return result

