from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://online.actitime.com/capgemini1/login.do")
driver.implicitly_wait(20)
sleep(2)
username=driver.find_element_by_id("username")
action =ActionChains(driver)
action.move_to_element(username)
action.key_down(Keys.SHIFT)
action.send_keys("n")
action.key_up(Keys.SHIFT).perform()
