# tools-group-project README
### Description of the project
The goal of the project is to build a personalized recommendation system helping people who is planning travels find the best travel package consist of hotels and flights. The customer can input the place of departure, destination, start date, end date and budget, and the recommendation system can provide sorted travel packages including departure flght, return flight and hotel. There are 3 diffenrent ranking criterion when sorting travel packages which are total price of the package (1), rating of the hotel (2) and recommendation score (3).

**The main steps**
1. Input user information including departure city, destination, travel duration, budget and number of travelers.
2. Get qualified flight info from Expedia, Hotwire, Priceline and Hipmunk.
3. Get qualified hotel info from Airbnb and Booking.
4. Combine flight and hotel info then filter to generate travel packages.
5. Sort the packages by price, rating and recommendation.

**the ranking criterion**
1. Rank the packages by the total price of hotel and roundtrip flight, if the total price is the same, then rank them by the rating of the hotel, which is the ranking criteria (2). 
2. Rank the packages by the rating of the hotel, if the rating of the hotel is the same, then rank them by the total price of the package, which is the ranking criteria (1).
3. Rank the packages by the recommendation score by assigning weight to price (20%), rating(40%), comment number(40%). 


**About the result**
1. The result is printed in the form of data frame, and each row represents a travel package including the detailed information of the hotel, departing flight and return flight, each column represents a variable like airline, airport, time, hotel name, rating, comments, price, etc. 
2. The result is saved as pictures and can be accessed by the following link: link:https://pan.baidu.com/s/1KYrYCbO5GeW1QyyY9uVXoA  password:l9z8


### Group name and Section:
**Contributors (in random order)**
Mingshan Zhang (mz2701)
Yue Li (yl4015)
Xinyue Shi (xs2349)
Xiaohan Liu (xl2838)

**Section**
Sec 002


### Installation Instruction:
1)	Installation
Since expedia and hotwire are static web page in which python can use a combination of libraries as requests and BeautifulSoup. We need to get the BeautifulSoup library using pip, a package management tool for python.
We type:

```
!pip install BeautifulSoup

```

Note: If you fail to execute the above command line try adding sudo in front of each line.

Since the remaining four web pages as priceline (flight), hipmunk (flight), Booking (hotel), Airbnb (hotel) are dynamic loading web pages in which python cannot scrape the complete source code of the web page, so we install a new library selenium
We type:

```
!pip install selenium

```

2)	Import packages

```
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
```

### Run Instructions:
1. the main_program.py is the only program that we need to run, other py files are used to be integrated into the main function (generate_packages);
2. To start the program, we need to input the traveler’s information in the input module, including departure city, departure country, destination city code, destination city, destination country, destination code, depart date (MM-DD-YYYY), return date (MM-DD-YYYY), budget, number of adults, number of children, the sorting method (0:by price,1:by rating,2:by recommendation). Format of these input variables need to be paid attention to;
3. For the chromedriver in selenium, we need to download chromedriver.exe and add the path into the parenthesis of driver = webdriver.chrome();
4. It is possible that we visit the web page frequently so that the “robot check “error might be raised, indicating that we visit too frequently to be recognized as an robot, wait for a while before next try may solve this problem;
5. It is possible that opening the webpage and the clicking process might take some time, so please be patient for it to process and do not close the window before it’s done.




