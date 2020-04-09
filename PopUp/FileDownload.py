#handle file download pop up

from selenium import webdriver
import keyboard
from time import sleep
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.seleniumhq.org/download/")
link=driver.find_element_by_link_text("3.141.59")
link.click()
keyboard.press_and_release("tab")
sleep(2)
keyboard.press_and_release('tab')
sleep(2)
keyboard.press_and_release('enter')
