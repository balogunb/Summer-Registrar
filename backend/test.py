#Given a link to a course catalog, this script allows you get select a 
#term and takes you to the page containing all courses 


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


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

#browser = webdriver.Chrome();
#browser.get("google.com")
#print('testing123')




from pymongo import MongoClient





link = "mongodb+srv://Basitb:"+ password+ "@collegecourses-ne1ze.mongodb.net/test?retryWrites=true&w=majority"
print(link)
client = MongoClient(link)
db = client.CollegeCourses


schools_courses = {
	'courseName' : "Test1111",
	'school' : " ",
	'term' : " ",
	'year' : " ",
	'CRN' : " ",
	'description' : " ",
	'section' : " ",
	'zipcode' : " "
	}
db.Courses.insert_one(schools_courses)
    	
	