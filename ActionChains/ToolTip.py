from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
def toolTipUsingTitle():
    driver.get("http://demoqa.com/tooltip/")
    sleep(2)
    age=driver.find_element_by_id("age")
    tooltipText=age.get_attribute("title")
    print(tooltipText)
    expectedText="We ask for your age only for statistical purposes."
    if tooltipText==expectedText:
        print("ToolTip text is correct")
    else:
        print("ToolTip text is not correct")
# toolTipUsingTitle()
def toolTipTextUsingActionChains():
    driver.get("http://demoqa.com/tooltip-and-double-click/")
    age=driver.find_element_by_id("tooltipDemo")
    action=ActionChains(driver)
    action.move_to_element(age).perform()
    toolTip=driver.find_element_by_css_selector(".tooltiptext")
    toolTipText=toolTip.text
    expectedText = "We ask for your age only for statistical purposes."
    if toolTipText==expectedText:
        print("ToolTip text is correct")
    else:
        print("ToolTip text is not correct")
toolTipTextUsingActionChains()