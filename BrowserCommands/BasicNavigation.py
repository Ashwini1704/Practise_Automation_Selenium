from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
sleep(2)
driver.get("https://wwww.google.com")
#to maximize the chrome window
driver.maximize_window()
sleep(2)
#to navigate back to the url which is opened previously i.e,facebook
driver.back()
sleep(2)
#to navigate to forard url which is opened i.e,google
driver.forward()
sleep(2)
# Refresh the web page
driver.refresh()
sleep(2)
#close the browser
driver.close()

