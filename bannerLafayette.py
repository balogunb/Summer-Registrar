from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


class SubjectInfo:
    school = 'Lafayette'
    term ='Summer I 2019' #ie summer 2019
    name = '' #class Name
    code = '' #course code for the subject
    section = '' #course section ID
    regDate  = 'Sep 05,2018 to Jul 05,2019'#registration date
    attribute = '' #course attribute ie Social Science Outcome
    location = '' #where the class is going to hold
    days = '' # days lecture would be held
    time = '' #time class would hold
    duration = '' #the date range for the class
    type = ''  #usually lecture
    instructor = '' #instructor in charge of the class
















#launch browser and go to website
browser = webdriver.Chrome();
browser1 = webdriver.Chrome();
browser.get('https://bannerselfservice.lafayette.edu/pls/bprod/bwckschd.p_disp_dyn_sched')
browser1.get('https://bannerselfservice.lafayette.edu/pls/bprod/bwckschd.p_disp_dyn_sched')

#selects the summer option
term = browser.find_element_by_xpath("//option[@value='201840']")
term.click()
term1 = browser1.find_element_by_xpath("//option[@value='201850']")
term1.click()

#clicks submit
browser.find_element_by_xpath("//input[@type ='submit']").click()
browser1.find_element_by_xpath("//input[@type ='submit']").click()



#class schedule search page, put all contents of select in a list
subjects = Select(browser.find_element_by_xpath("//select[@name ='sel_subj']"))
subjectList = subjects.options


subjects1 = Select(browser1.find_element_by_xpath("//select[@name ='sel_subj']"))
subjectList1 = subjects1.options


#highlight all subject
for x in subjectList:
    subjects.select_by_value(x.get_attribute("value"))
    #print(x.get_attribute("value"))

for x in subjectList1:
    subjects1.select_by_value(x.get_attribute("value"))


#clicks submit this leads to the page containing the course schedules
browser.find_element_by_xpath("//input[@type ='submit']").click()
browser1.find_element_by_xpath("//input[@type ='submit']").click()

#SCRAPING BEGINS
soup = BeautifulSoup(browser.page_source,'html.parser')     #beautifulsoup4 if needed


sectionTag = [] #contains objects which store SubjectInfo
#sectionTag1 = [] #contains objects which store SubjectInfo

titles =  browser.find_elements_by_xpath("//th[@class='ddtitle']")
titles1 =  browser1.find_elements_by_xpath("//th[@class='ddtitle']")

#Add all subject names to sectionTag
for x in titles:
    subject = SubjectInfo()
    details =  x.find_element_by_tag_name('a').text
    detailsList = details.split(' - ')
    subject.name = detailsList[0]
    subject.code = detailsList[1]
    subject.section = detailsList[2] + " - " + detailsList[3]
    sectionTag.append(subject)



for x in titles1:
    subject = SubjectInfo()
    details =  x.find_element_by_tag_name('a').text
    detailsList = details.split(' - ')
    subject.name = detailsList[0]
    subject.code = detailsList[1]
    subject.section = detailsList[2] + " - " + detailsList[3]
    sectionTag.append(subject)

for y in sectionTag:
    print(y.name)


#sections = browser.find_elements_by_xpath("/html/body/div/table/tbody/tr/td/table/tbody/tr[2]")

#for y in sections:
#    print(y.find_element_by_xpath("//td[@class = 'dddefault']").text)


#print(len(sections))




    #count++









browser.quit()
