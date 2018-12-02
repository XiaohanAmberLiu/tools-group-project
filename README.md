# tools-group-project
Tools for analytics 2018, members include Xiaohan Liu, Mingshan Zhang, Yue Li, Xinyue Shi
###Description of the project:
The goal of the project is a personalized recommendation system helping people who is planning travels find the best travel package consisting of hotels and flights. The customer can input the place of departure, destination, start date, end date and budget, and the recommendation system can output ranked travel packages according to different ranking criterion. There are 3 ranking criterion which are price of the package (1), rating of the hotel (2) and recommendation weighted score (3).

About the ranking criterion: 
(1)	Rank the packages by the total price of hotel and roundtrip flight, if the total price is the same, then rank them by the rating of the hotel, which is the ranking criteria (2). 
(2)	Rank the packages by the rating of the hotel, if the rating of the hotel is the same, then rank them by the total price of the package, which is the ranking criteria (1).
(3)	Rank the packages by the recommendation score by assigning weight to price (20%), rating(40%), comment number(40%). 



The result is printed in the form of data frame, and each row represents a travel package including the detailed information of the hotel, departing flight and return flight, each column represents a variable like airline, airport, time, hotel name, rating, comments, price, etc.

The main steps are:
1. Input user information including departure city, destination, travel duration, budget and number of travelers.
2. Get qualified flight info from Expedia, Hotwire, Priceline and Hipmunk.
3. Get qualified hotel info from Airbnb and Booking.
4. Combine flight and hotel info then filter to generate travel packages.
5. Sort the packages by price, rating and recommendation.

Group name and Section:
Contributors (in random order): 
Mingshan Zhang (mz2701)
Yue Li (yl4015)
Xinyue Shi (xs2349)
Xiaohan Liu (xl2838)
Section: Sec 002


Installation Instruction:
1)	Installation
Since expedia and hotwire are static web page in which python can use a combination of libraries as requests and BeautifulSoup. We need to get the BeautifulSoup library using pip, a package management tool for python.
We type:
!pip install BeautifulSoup

Note: If you fail to execute the above command line try adding sudo in front of each line.

Since the remaining four web pages as priceline (flight), hipmunk (flight), Booking (hotel), Airbnb (hotel) are dynamic loading web pages in which python cannot scrape the complete source code of the web page, so we install a new library selenium
We type:
!pip install selenium
2)	Import packages


Python 
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


Run Instructions:

	It is possible that we visit the web page frequently so that the “robot check “error might be raised, indicating that we visit too frequently to be recognized as an robot, wait for a while before next try may solve this problem.
	It is possible that opening the webpage and the clicking process might take some time, so please be patient for it to process and do not close the window before it’s done.










Contributor guidelines:

