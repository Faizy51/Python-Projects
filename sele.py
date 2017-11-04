from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Firefox()

driver.get("https://www.freshersworld.com/user/my-callletter")
user = driver.find_element_by_id('emailview')
user.send_keys('faizulla49g@gmail.com')
password = driver.find_element_by_id('passwordview')
password.send_keys('freshersworld')
login = driver.find_element_by_css_selector('#loginSubmitView')
url = driver.current_url
login.click()
if url == driver.current_url:
    login.click()
time.sleep(10)


while True:
    time.sleep(5)
    driver.get("https://www.freshersworld.com/user/my-callletter")
    # to select the option
    loc = driver.find_element_by_id('call_letter_changestatus-90225')
    select = Select(loc).select_by_value('1')



    
