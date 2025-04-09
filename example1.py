


from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.implicitly_wait(10) #this will wait for 10 seconds before throwing an exception and it is a global wait
driver.maximize_window() #this will maximize the window

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
message = driver.find_element(By.CSS_SELECTOR, ".red").text
var = message.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID, "username").send_keys(var)
driver.find_element(By.ID, "password").send_keys(var)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)