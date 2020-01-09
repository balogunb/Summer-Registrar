#Given a link to a course catalog, this script allows you get select a 
#term and takes you to the page containing all courses 


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait



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



def getCatalogPage(website):

	#make the browser headless
	#chrome_options = Options()
	#chrome_options.add_argument("--headless")
	#chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'
	#driver = webdriver.Chrome(  chrome_options=chrome_options)

	#launch browser and go to website
	#browser = webdriver.Chrome(chrome_options=chrome_options);
	#browser1 = webdriver.Chrome(chrome_options=chrome_options);
	#browser.get('https://bannerselfservice.lafayette.edu/pls/bprod/bwckschd.p_disp_dyn_sched')
	#browser1.get('https://bannerselfservice.lafayette.edu/pls/bprod/bwckschd.p_disp_dyn_sched')

	browser = webdriver.Chrome();
	browser.get(website)

	#selects the term and submit
	#termlist = browser.find_element_by_xpath("//select[@name='p_term']")
	#termlist.click()
	term = browser.find_element_by_xpath("//option[@value='201920']")
	term.click()
	browser.find_element_by_xpath("//input[@type ='submit']").click()

	#class schedule search page, put all contents of select in a list
	subjects = Select(browser.find_element_by_xpath("//select[@name ='sel_subj']"))
	subjectList = subjects.options

	#highlight all subject
	for x in subjectList:
	    subjects.select_by_value(x.get_attribute("value"))
	    #print(x.get_attribute("value"))

	#clicks submit this leads to the page containing the course schedules
	browser.find_element_by_xpath("//input[@type ='submit']").click()

	return browser





def scrapePage(browser):
	body = browser.find_element_by_xpath("//div[@class ='pagebodydiv']")
	courseList = body.find_element_by_tag_name('tbody')
	courseTitles = courseList.find_elements_by_class_name('ddtitle')
	courseContents = courseList.find_elements_by_xpath("/html/body/div[@class='pagebodydiv']/table[@class='datadisplaytable'][1]/tbody/tr/td")
	
	print(len(courseTitles))
	print(len(courseContents))	
	scrapeInfo(courseTitles,courseContents)
	#soup = BeutifulSoup(txt, 'lxml')



def scrapeInfo(titlesList,contentList):
	for x in range(len(titlesList)):
		subj = scrapeTitle(titlesList[x])

	



def scrapeTitle(titleDom):
	subject = SubjectInfo()
	details = titleDom.find_element_by_tag_name('a').text
	detailsList = details.split(' - ')
	subject.courseName = detailsList[0]
	subject.CRN = detailsList[1]
	subject.section = detailsList[2] + " - " + detailsList[3]
	#sectionTag.append(subject)
	print(subject)
	
	



#def scrapeBody(bodyDom):




