from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

#browser = webdriver.Chrome()
#browser.get('https://automatetheboringstuff.com')

browser = webdriver.Chrome();
browser.get('https://bannerselfservice.lafayette.edu/pls/bprod/bwckschd.p_disp_dyn_sched')


#selects the summer option
term = browser.find_element_by_xpath("//option[@value='201840']")
term.click()


#clicks submit
browser.find_element_by_xpath("//input[@type ='submit']").click()




#class schedule search page
#highlight all subject

subjects = Select(browser.find_element_by_xpath("//select[@name ='sel_subj']"))
#subjects = browser.find_element_by_xpath("//select[@name ='sel_subj']")
subjectList = subjects.options

for x in subjectList:
    subjects.select_by_value(x.get_attribute("value"))
    #print(x.get_attribute("value"))


#clicks submit
browser.find_element_by_xpath("//input[@type ='submit']").click()




#browser.quit()
