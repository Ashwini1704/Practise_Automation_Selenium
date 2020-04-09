from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Ashwini/Desktop/HTML_Files/dropdown.html")
driver.maximize_window()
dropdown=driver.find_element_by_name("D1")
#creating an object for select class
select=Select(dropdown)
sleep(2)
def optionsFunc():
    allOption=select.options
    print(len(allOption))
    for i in allOption:
        print(i.text)
# optionsFunc()
def is_multipleFunc():
    if select.is_multiple:
        print("The dropdown is multiple")
    else:
        print("The dropdown is single")
# is_multipleFunc()

driver.close()