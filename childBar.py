from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

driver.implicitly_wait(10) #this will wait for 10 seconds before throwing an exception and it is a global wait
driver.maximize_window() #this will maximize the window

driver.find_element(By.LINK_TEXT,"Click Here").click() #this will click on the element with link text Click Here

windowsopen = driver.window_handles  # this will get the list of all the open windows by automation  and index start from 0
driver.switch_to.window(windowsopen[1]) #this will switch the control to the new window

print(driver.find_element(By.TAG_NAME,"h3").text) #this will get the text of the element with tag name h3
driver.close() #this will close the current window

driver.switch_to.window(windowsopen[0]) #this will switch the control to the first window
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text