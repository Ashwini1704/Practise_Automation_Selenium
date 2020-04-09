from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://online.actitime.com/capgemini1/login.do")

driver.implicitly_wait(15)
usn=driver.find_element_by_id("username")
usn.send_keys("nandeesha.kiccha0@gmail.com")
pwd=driver.find_element_by_name("pwd")
pwd.send_keys("Logistics@123")
wait=WebDriverWait(driver,10)
loginButton=wait.until(ec.element_to_be_clickable((By.ID,'loginButton')))
loginButton.click()
driver.close()