#using click(self,web element) from ActionChains class
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.irctc.co.in")
sleep(2)
action=ActionChains(driver)
def clickFunc():
    trains=driver.find_element_by_xpath("//a[text()=' TRAINS ']")
    action.move_to_element(trains).perform()
    cancelTicket=driver.find_element_by_xpath("//span[text()='Cancel Ticket']")
    eTicket=driver.find_element_by_xpath("//span[text()='E-tickets']")
    action.move_to_element(cancelTicket).click(eTicket).perform()
# clickFunc()
def move_by_offsetFunc():
    trains = driver.find_element_by_xpath("//a[text()=' TRAINS ']")
    loc = trains.location
    x = loc.get("x")
    y = loc.get("y")
    action.move_by_offset(x, y).perform()
driver.close()