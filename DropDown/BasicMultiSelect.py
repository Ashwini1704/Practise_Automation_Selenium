#select the options from multi-select dropdown
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Ashwini/Desktop/HTML_Files/multipleDropDown.html")
driver.maximize_window()
dropdown=driver.find_element_by_name("D1")
select=Select(dropdown)
sleep(2)
select.select_by_visible_text("Dosa")
sleep(2)
select.select_by_value("Puri")
sleep(2)
select.select_by_index(4)
sleep(2)
select.deselect_by_index(2)
sleep(2)
select.deselect_by_value("Upma")
sleep(2)
select.deselect_by_visible_text("Puri")
driver.close()