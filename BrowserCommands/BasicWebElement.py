from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
def displayedFunc():
    driver.get("https://www.google.com")
    googleImage=driver.find_element_by_id("hplogo")
    res=googleImage.is_displayed()
    if res:
        print("The element is displayed")
    else:
        print("The element is not displayed")
#displayedFunc()
def enabledFunc():
    driver.get("https://www.google.com")
    googleSearch=driver.find_element_by_name("btnK")
    value=googleSearch.is_enabled()
    if value:
        print("The element is enabled")
    else:
        print("The element is not enabled")
# enabledFunc()
def selectedFunc():
    driver.get("https://online.actitime.com/capgemini1/login.do")
    checkbox=driver.find_element_by_id("keepLoggedInCheckBox")
    result=checkbox.is_selected()
    if result:
        print("The element is selected")
    else:
        print("The element is not selected")
#selectedFunc()
def clearFunc():
    driver.get("https://online.actitime.com/capgemini1/login.do")
    sleep(2)
    username = driver.find_element_by_id("username")
    username.send_keys("nandeesha.kiccha0@gmail.com")
    sleep(2)
    username.clear()
# clearFunc()
def getAttributeAndTagNameFunc():
    driver.get("https://online.actitime.com/capgemini1/login.do")
    sleep(2)
    username = driver.find_element_by_id("username")
    username.send_keys("nandeesha.kiccha0@gmail.com")
    print("Attribute value of value attribute is",username.get_attribute("value"))
    print("Tag name of username field",username.tag_name)
    sleep(3)
    driver.close()
#getAttributeAndTagNameFunc()
def size_location_rectFunc():
    driver.get("https://online.actitime.com/capgemini1/login.do")
    sleep(2)
    pleaseText = driver.find_element_by_id("headerContainer")
    print("The text is ", pleaseText.text)
    print("size==>", pleaseText.size)
    print("location==>", pleaseText.location["x"], pleaseText.location["y"])
    print("rect is", pleaseText.rect)
    sleep(3)
    driver.close()
# size_location_rectFunc()
def findElemnents_getPropertyFunc():
    driver.get("https://www.bbc.com")
    sleep(2)
    linkslist = driver.find_elements_by_xpath("//a")
    print(len(linkslist))
    for i in linkslist:
        url = i.get_property("href")
        print(url)
    sleep(5)
    driver.close()
# findElemnents_getPropertyFunc()