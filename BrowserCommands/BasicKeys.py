from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://online.actitime.com/capgemini1/login.do")
sleep(2)
username=driver.find_element_by_id("username")
username.send_keys("nandeesha.kiccha0@gmail.com")
password=driver.find_element_by_name("pwd")
password.send_keys("Logistics@123")
loginButton=driver.find_element_by_id("loginButton")
loginButton.send_keys(Keys.ENTER)
driver.close()