from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')

browser2 = webdriver.Chrome();
browser2.get('https://bannerselfservice.lafayette.edu/pls/bprod/bwckschd.p_disp_dyn_sched')
