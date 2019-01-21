from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

email = 'Your email'
pw = 'Your password'

message = input('What message do you want to post on facebook?  >  ')
time.sleep(3)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.facebook.com")

driver.find_element_by_xpath('//*[@id="pass"]').send_keys(pw)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)

driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

driver.find_element_by_xpath("//textarea[@name='xhpc_message']").send_keys(message)
time.sleep(1)
driver.find_element_by_class_name('_6c0o').click()



