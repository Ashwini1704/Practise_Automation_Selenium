from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
#title of the webpage
actualTitle=driver.title
print("Title of the page",actualTitle)
print("The length of the title is",len(actualTitle))
#current url of the webpage
url=driver.current_url
print(url)
if url == "https://www.facebook.com/":
    print("Correct URL is opened")
else :
    print("Correct URL is not opened")
#page source of the page
pageSource=driver.page_source
print("Length of the page source is",len(pageSource))
#close browser
driver.close()