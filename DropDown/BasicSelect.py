from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Ashwini/Desktop/HTML_Files/dropdown.html")
driver.maximize_window()
dropdown=driver.find_element_by_name("D1")
#creating an object for select class
select=Select(dropdown)
#selecting using index
select.select_by_index(2)
sleep(2)
select.select_by_index(0)
sleep(2)
#selecting using value
select.select_by_value("Puri")
sleep(2)
select.select_by_value("Dosas")
sleep(2)
#selecting using visible text
select.select_by_visible_text("Idly")
sleep(2)
select.select_by_visible_text("Upma")
sleep(2)

driver.close()