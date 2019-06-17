from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


#launch browser and go to website
browser = webdriver.Chrome();
browser.get('https://bannerselfservice.lafayette.edu/pls/bprod/bwckschd.p_disp_dyn_sched')


#selects the summer option
term = browser.find_element_by_xpath("//option[@value='201840']")
term.click()

#clicks submit
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


#SCRAPING BEGINS
soup = BeautifulSoup(browser.page_source)#beautifulsoup4 if needed


sectionTag = [] #contains all the class names
sections =  browser.find_elements_by_xpath("//th[@class='ddtitle']")
for x in sections:
    sectionTag.append( x.find_element_by_tag_name('a'))

for y in sectionTag:
    print(y.text)


#browser.quit()
