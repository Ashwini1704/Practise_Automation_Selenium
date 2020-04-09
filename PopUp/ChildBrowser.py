#to handle child browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://online.actitime.com/capgemini1/login.do")
#fetch the current window address on which the driver is having control
parent_window=driver.current_window_handle
driver.implicitly_wait(10)
#the parent browser, click on the link in new window(child browser)
link=driver.find_element_by_link_text("actiTIME Inc.")
link.send_keys(Keys.SHIFT+Keys.ENTER)
#fetch all the windows address which is launched at the time of execution irrespective of the control of the driver on browser
all_window=driver.window_handles
#remove parent from all_window
all_window.remove(parent_window)
#switch the control to the child browser
driver.switch_to.window(all_window[0])
#click on the link "Why actiTIME"
link1=driver.find_element_by_link_text("Why actiTIME")
link1.click()
