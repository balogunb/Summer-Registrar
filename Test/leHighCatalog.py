#scrapes data from lehigh's catalog

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from pymongo import MongoClient

import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()


class SubjectInfo:
    school = 'LEHIGH'
    term ='' #ie summer 2019
    name = '' #class Name
    code = '' #course code for the subject
    section = '' #course section ID
    regDate  = ''#registration date
    attribute = '' #course attribute ie Social Science Outcome
    location = '' #where the class is going to hold
    days = '' # days lecture would be held
    time = '' #time class would hold
    duration = '' #the date range for the class
    type = ''  #usually lecture
    instructor = '' #instructor in charge of the class

'''
    #make the browser headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    #launch browser and go to website
    browser = webdriver.Chrome(chrome_options=chrome_options);
'''



browser = webdriver.Chrome();
browser.get('https://registration.lehigh.edu/StudentRegistrationSsb/ssb/classSearch/classSearch')

#click submit

#element.sendKeys('2019')

#searchInput = browser.find_element_by_tag_name('input')
#searchInput.send_keys('2019 Summer Semester')
#print(browser.find_elements_by_xpath("//li[@id ='select2-result-label-3']").getId())
