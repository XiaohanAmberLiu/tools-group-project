
# coding: utf-8

# In[3]:

#destination,adult_num,child_num,cktin_date,cktout_date,budget
url='https://www.booking.com/'
cktin_date='2019-02-14'
cktout_date='2019-02-21'
adult_num=1
child_num=0
destination='Paris'


# In[4]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
import time
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('/Users/zhangmingshan/Desktop/2018 Autumn/Tools for Analytics/Project/chromedriver')
try:
    driver.get(url)
except:
    print("Connection Failure")
driver.maximize_window()
driver.implicitly_wait(5)


# In[5]:

#Set destination
dest=driver.find_element_by_xpath("//input[@type='search']")
dest.send_keys(destination)


# In[6]:

#open calender
cals=driver.find_elements_by_xpath("//button[@aria-label='Open calendar']")
cals[0].click()


# In[7]:

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


# In[8]:

start_dates=driver.find_elements_by_xpath("//td[@class='bui-calendar__date'][@data-bui-ref='calendar-date']")
#click checkin date
for start_date in start_dates:
    if cktin_date.strip() == start_date.get_attribute('data-date').strip():
        start_date.click()

#click checkout date
for start_date in start_dates:
    if cktout_date.strip() == start_date.get_attribute('data-date').strip():
        start_date.click()


# In[9]:

import re
person_button=driver.find_element_by_xpath("//label[@for='xp__guests__input']")
person_button.click()

#adult
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


# In[10]:

#click submit
submit=driver.find_element_by_xpath("//button[@type='submit'][@data-sb-id='main']")
submit.click()
        


# In[ ]:

def set_basic_info()

