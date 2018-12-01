
# coding: utf-8

# In[6]:

#send basic info to booking
def set_basic_info(destination,adult_num,child_num,cktin_date,cktout_date):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import Select
    import re
    import time
    import re
    
    url='https://www.booking.com/'
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome('/Users/zhangmingshan/Desktop/2018 Autumn/Tools for Analytics/Project/chromedriver')
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
                if adult_web>adult_num:
                    sub_button[0].click()
                elif adult_web<adult_num:
                    add_button[0].click()

                if child_web>child_num:
                    sub_button[1].click()
                elif child_web<child_num:
                    add_button[1].click()
            except:
                select_a = Select(driver.find_element_by_name('group_adults'))
                select_a.select_by_value(str(adult_num))
                select_c = Select(driver.find_element_by_name('group_children'))
                select_c.select_by_value(str(child_num))
                break
                
                
        else:
            break
    
    #click submit
    submit=driver.find_element_by_xpath("//button[@type='submit'][@data-sb-id='main']")
    submit.click()
    
    return driver


# In[7]:

#destination,adult_num,child_num,cktin_date,cktout_date,budget
cktin_date='2019-02-14'
cktout_date='2019-02-21'
adult_num=1
child_num=0
destination='Paris'
driver=set_basic_info(destination,adult_num,child_num,cktin_date,cktout_date)


# In[5]:

#def get_page_info(url,budget,page_total_num=1): 

budget=1000
page_total_num=1


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
            print(p)

#             if p<=budget:
#                 #get hotel url
#                 try:
#                     link=Hotel.find_elements_by_xpath("//a[@class='hotel_name_link url']")
#                     l=link[0].get_attribute('href')
#                 except:
#                     l=""

#                 #get hotel name
#                 try:
#                     name=Hotel.find_elements_by_class_name('sr-hotel__name')
#                     n=name[0].text
#                 except:
#                     n=""

#                 #get hotel description
#                 try:
#                     Descrips=Hotel.find_elements_by_class_name('room_link')
#                     d=Descrips[0].text
#                     d=d.replace('\n',' · ')
#                 except:
#                     d=""

#                 #rating
#                 try:
#                     rating=Hotel.find_elements_by_class_name('bui-review-score__badge')
#                     r=rating[0].text
#                 except:
#                     r=""

#                 ##num of reviews
#                 try:
#                     review=Hotel.find_elements_by_class_name('bui-review-score__text')
#                     rev=re.match(r'\d+',review[0].text.replace(',','')).group()

#                 except:
#                     rev=""
                    
#                 result.append((n,p,r,rev,d,l))
#             else:
#                 continue

        except:
            continue

    page += 1  
    driver.find_element_by_xpath("//li[@class='bui-pagination__item bui-pagination__next-arrow']").click()
    driver.refresh()

# #driver.close()
# result
#return result



# In[4]:

driver.close()

