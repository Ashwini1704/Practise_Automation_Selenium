#disable notification pop up
from selenium import webdriver
option=webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cleartrip.com")
