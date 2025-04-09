from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(10) #this will wait for 10 seconds before throwing an exception and it is a global wait
driver.maximize_window() #this will maximize the window

action = ActionChains(driver)

#action.double_click(driver)
#action.click_and_hold(driver)
#action.context_click(driver)
#action.drag_and_drop(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform() #this will move the mouse to the element with id mousehover
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()  #this will right click on the element with link text Top
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform() #this will move the mouse to the element with link text Reload and click on it
time.sleep(5)