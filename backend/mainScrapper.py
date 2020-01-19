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
courseList = bs.scrapePage(browser)
store(courseList)


def store(cList):
	#Get env variables
	dotenv_path = join(dirname(r'''C:\Users\Basit\OneDrive\Summer 2019 Projects and Courses\Summer-Registrar\backend'''), '.env')
	load_dotenv(dotenv_path)
	







# Accessing variables.
password = os.getenv('PASSWORD')

print(password)
#Store all data in database
#print('Insert password')
#password = input()


link = "mongodb+srv://Basitb:" + password + "@collegecourses-ne1ze.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(link)
db = client.schools_courses

for course in sectionTag:
    schools_courses = {
    'name' : course.name,
    'code' : course.code,
    'section' : course.section


    }
    db.Lafayette_College.insert_one(schools_courses) 
	
