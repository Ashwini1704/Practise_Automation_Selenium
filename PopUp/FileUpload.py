#handling file upload pop-up
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Ashwini/Desktop/HTML_Files/FileUpload.html")
fileSelected=driver.find_element_by_name("f1")
fileSelected.send_keys("C:\\Users\\Ashwini\\Desktop\\HTML_Files")
uploadButton=driver.find_element_by_xpath("//input[@type='submit']")
uploadButton.click()