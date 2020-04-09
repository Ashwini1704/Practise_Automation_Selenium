#select the options from multi-select dropdown, print the selected options and its count
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
def all_selected_optionsFunc():
    selectedOptions=select.all_selected_options
    print(len(selectedOptions))
    for i in selectedOptions:
        print(i.text)
# all_selected_optionsFunc()
def first_selected_optionFunc():
    firstSelectedOption = select.first_selected_option
    print(firstSelectedOption.text)
# first_selected_optionFunc()
sleep(2)
driver.close()

