#action chanins class for trains for irctc app
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.irctc.co.in")

sleep(2)
action=ActionChains(driver)
trains=driver.find_element_by_xpath("//a[text()=' TRAINS ']")
action.move_to_element(trains).perform()
cancelTicket=driver.find_element_by_xpath("//span[text()='Cancel Ticket']")
action.move_to_element(cancelTicket).perform()
eTicket=driver.find_element_by_xpath("//span[text()='E-tickets']")
eTicket.click()
driver.close()
