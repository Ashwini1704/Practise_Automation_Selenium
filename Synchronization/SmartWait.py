from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://online.actitime.com/capgemini1/login.do")
wait=WebDriverWait(driver,10,poll_frequency=5,
                   ignored_exceptions=["ElementNotVisibleException"])
username=wait.until(EC.element_to_be_clickable((By.ID,"username")))
username.send_keys("asd")
windowHandles=driver.window_handles
print(type(windowHandles),windowHandles)