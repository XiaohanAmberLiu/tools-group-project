
# coding: utf-8

# In[1]:

city = 'Paris'
cktin_year = '2019'
cktin_month = '02'
cktin_day = '14'
cktout_year = '2019'
cktout_month = '02'
cktout_day = '21'
rooms = '1'
adults = '2'
children = '0'
url = "https://www.expedia.com/Hotel-Search?destination="+city+"&startDate="+cktin_month+"%2F"+cktin_day+"%2F"+cktin_year+"&endDate="+cktout_month+"%2F"+cktout_day+"%2F"+cktout_year+"&rooms="+rooms+"&adults="+adults+""
url


# In[2]:

def get_page_info(url,budget,page_total_num):
    
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    import re
    import pandas as pd
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(r"C:\Users\shixinyue\Desktop\Columbia University\Tools for Analytics\web crawler\chromedriver")
    try:
        driver.get(url)
    except:
        return "Connection Failure"
    driver.maximize_window()
    
    page = 1
    result = list()
    while page <= page_total_num:
        driver.implicitly_wait(30)
        hotels = driver.find_elements_by_xpath("//div[@class='flex-content  info-and-price MULTICITYVICINITY avgPerNight']")
        for hotel in hotels:
            description = ''
            pr = hotel.find_elements_by_class_name('actualPrice')[0].text
            price = int(re.search(r'\d+',pr).group())
            if price < budget:
                name = hotel.find_elements_by_class_name('hotelTitle')[0].text
                link = hotel.find_elements_by_xpath("//a[@class='flex-link']")[0].get_attribute('href')
                ratings = hotel.find_elements_by_class_name('starRating')
                try:
                    rating = ratings[0].text
                except:
                    pass
                rates = hotel.find_elements_by_class_name('reviewOverall')
                try:
                    rating = rates[0].text
                except:
                    pass
                reviews = hotel.find_elements_by_class_name('reviewCount')
                try:
                    review = reviews[1].text
                except:
                    review = ''
                links = hotel.find_elements_by_xpath("//a[@class='flex-link']")
                link = links[0].get_attribute('href')
                result.append((name,price,rating,review,description,link))
        page += 1
        driver.find_element_by_class_name('pagination-next').click()
        driver.refresh()

    driver.close()
    return result

