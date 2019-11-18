import selenium
from selenium import webdriver
driver = webdriver.Chrome
d = driver()
d.get('https://www.facebook.com/')
username = d.find_element_by_name("email")
username.send_keys('ckim6189@gmail.com')
Pass = d.find_element_by_name('pass')
Pass.send_keys('********') #put your password here
submit = d.find_element_by_id('u_0_2')
submit.click()