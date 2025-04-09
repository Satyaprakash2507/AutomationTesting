import time

from selenium import webdriver #this line will import the webdriver from selenium

driver = webdriver.Chrome()  #this line will open the browser

driver.get("https://rahulshettyacademy.com") #this line will hit the url

driver.maximize_window() #this line will maximize the window

print(driver.title) #this line will get the title of the page

print(driver.current_url) #this line will get the current url of the page

time.sleep(10) #this line will wait for 10 seconds before closing the browser