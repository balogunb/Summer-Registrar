

#SCRAPING BEGINS
soup = BeautifulSoup(browser.page_source,'html.parser')     #beautifulsoup4 if needed


sectionTag = [] #contains objects which store SubjectInfo

titles =  browser.find_elements_by_xpath("//th[@class='ddtitle']")

#Add all subject names to sectionTag
for x in titles:
    subject = SubjectInfo()
    details =  x.find_element_by_tag_name('a').text
    detailsList = details.split(' - ')
    subject.name = detailsList[0]
    subject.code = detailsList[1]
    subject.section = detailsList[2] + " - " + detailsList[3]
    sectionTag.append(subject)

#for y in sectionTag:
#    print(y.name)


#sections = browser.find_elements_by_xpath("/html/body/div/table/tbody/tr/td/table/tbody/tr[2]")

#for y in sections:
#    print(y.find_element_by_xpath("//td[@class = 'dddefault']").text)


#print(len(sections))




    #count++

browser.quit()
browser1.quit()


#Get env variables
dotenv_path = join(dirname(r'''C:\Users\Basit\OneDrive\Summer 2019 Projects and Courses\Summer_Project_2019'''), '.env')
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










    ///////////////////////////////////////
