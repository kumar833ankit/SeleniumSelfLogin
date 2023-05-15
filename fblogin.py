from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(r'C:\Users\B&O\Downloads\chromedriver (2).exe')
browser.get("https://www.facebook.com") 
time.sleep(10)
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
username.send_keys("aniketraj2002@rediffmail.com")
password.send_keys("")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

















