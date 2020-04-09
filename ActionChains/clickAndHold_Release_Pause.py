#click_and_hold, pause, release methods from ActionChains class
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://online.actitime.com/capgemini1/login.do")

sleep(2)
action =ActionChains(driver)
link=driver.find_element_by_link_text("actiTIME Inc.")
action.click_and_hold(link).perform()
action.pause(2)
action.release(link).perform()
driver.close()

sleep(2)
driver.close()