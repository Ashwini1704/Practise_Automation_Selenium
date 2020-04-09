#handle alert pop up
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Ashwini/Desktop/HTML_Files/alert.html")
clickMe=driver.find_element_by_xpath("//input[@type='button']")
clickMe.click()
#switch the control to the alert
alt=driver.switch_to.alert
altText=alt.text
print("Alert Text is ",altText)
#click on ok button
alt.accept()
#click on cancel button
# alt.dismiss()