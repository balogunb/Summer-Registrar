#from bs4 import BeautifulSoup
from pymongo import MongoClient
import LehighUniv as bs
import os
from os.path import join, dirname



class SubjectInfo:
    school = 'Lehigh University' #School name 
    zipcode = '18042' #School zipcode 
    term ='Summer' #ie summer 2019 maybe seperate year and term 
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






def store(cList):
    
	#Get env variables
	#dotenv_path = join(dirname(r'''C:\Users\Basit\OneDrive\Projects & courses\Summer-Registrar\backend'''), '.env') #So is this where you stored your password?
	#load_dotenv(dotenv_path) #??
	# Accessing variables.
	#password = os.getenv('PASSWORD')
	#print(password)
	#link = "mongodb+srv://Basitb:"+ password+ "@collegecourses-ne1ze.mongodb.net/test?retryWrites=true&w=majority"
	#print(link)
	#client = MongoClient(link)
	#db = client.CollegeCourses

    link = "mongodb+srv://Arithima:Lafayette23@collegecourses-ne1ze.mongodb.net/test?retryWrites=true&w=majority"
    print(link)
    client = MongoClient(link)
    db = client.CollegeCourses

    for course in cList:
        schools_courses = {
        'courseName' : course.courseName,
        'school' : course.school,
        'term' : course.term,
        'year' : course.year,
        'CRN' : course.CRN,
        'description' : course.description,
        'section' : course.section,
        'zipcode' : course.zipcode
        }
    db.LehighTest.insert_one(schools_courses)
    	



	
website = 'https://lewisweb.cc.lehigh.edu/PROD/bwckschd.p_disp_dyn_sched'
browser = bs.getCatalogPage(website)
courseList = bs.scrapePage(browser)
store(courseList)