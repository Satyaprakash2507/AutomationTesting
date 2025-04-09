from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

driver.implicitly_wait(10) #this will wait for 10 seconds before throwing an exception and it is a global wait
driver.maximize_window() #this will maximize the window

driver.switch_to.frame("mce_0_ifr") #this will switch the control to the iframe with id mce_0_ifr

driver.find_element(By.ID, "tinymca").clear() #clear the text in the text area
driver.find_element(By.ID, "tinymca").send_keys("Satya is automating the frames")


#switch back to default content
driver.switch_to.default_content() #this will switch the control back to the default content
print(driver.find_element(By.CSS_SELECTOR,"h3").text)