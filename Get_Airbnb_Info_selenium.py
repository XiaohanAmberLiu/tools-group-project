
# coding: utf-8

# In[8]:

def get_main_url(destination,adult_num,child_num,cktin_date,cktout_date):
    url="https://www.airbnb.com/s/"+destination+"/homes?adults="+adult_num+"&children="+child_num+"&checkin="+cktin_date+"&checkout="+cktout_date+"&refinement_paths%5B%5D=%2"+"Fhomes&allow_override%5B%5D=&s_tag=Vobyce0e"
    return url


# In[12]:

def get_page_info(url,budget,page_total_num=1): 
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    import re
    import pandas as pd

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome('/Users/zhangmingshan/Desktop/2018 Autumn/Tools for Analytics/Project/chromedriver')
    try:
        driver.get(url)
    except:
        return "Connection Failure"
    driver.maximize_window()
    
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
                pass
                  
        page += 1  
        driver.find_element_by_class_name('_1rltvky').click()
        driver.refresh()
    
    driver.close()
    return result


# In[13]:

def get_airbnb_list(destination,adult_num,child_num,cktin_date,cktout_date,budget):
    url=get_main_url(destination,adult_num,child_num,cktin_date,cktout_date)
    return get_page_info(url,budget,page_total_num=1)


# In[14]:

#example
get_airbnb_list('Paris','1','0','2019-02-14','2019-02-21',600)


# In[ ]:



