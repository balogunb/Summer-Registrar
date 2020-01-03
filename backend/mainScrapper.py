from bs4 import BeautifulSoup
from pymongo import MongoClient
import baseScrapper as bs
import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()


class SubjectInfo:
    school = 'Lafayette College' #School name 
    zipcode = '18042' #School zipcode 
    term ='Winter/Interim' #ie summer 2019 maybe seperate year and term 
    year = '2020'
    department = '' # ie humanities etc 
    courseName = '' #class Name
    CRN = '' #course registration number for the subject
    section = '' #course section ID
    regDate  = ''#registration date
    attribute = '' #course attribute ie Social Science Outcome
    location = '' #where the class is going to hold
    dateRange = ''
    description = '' # course description
    days = '' # days lecture would be held
    time = '' #time class would hold
    duration = '' #the date range for the class
    type = ''  #usually lecture
    instructor = '' #instructor in charge of the class
    prereq = ''
    regDeadline = '' #registration deadline



website = 'https://bannerselfservice.lafayette.edu/pls/bprod/bwckschd.p_disp_dyn_sched'
browser = bs.getCatalogPage(website)
bs.scrapePage(browser)


#print(browser.page_source)