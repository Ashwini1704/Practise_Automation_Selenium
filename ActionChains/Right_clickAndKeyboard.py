#right click using ActionChains class
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import keyboard

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://online.actitime.com/capgemini1/login.do")
sleep(2)
action =ActionChains(driver)
link=driver.find_element_by_link_text("actiTIME Inc.")
action.context_click(link).perform()
action.pause(2).perform()
#opeing in new tab and the tab is opened in backend,
# backend means the control of driver is on main page instead of new page
#keyboard.press('t')
#opening in new window
keyboard.press("w")
driver.close()

