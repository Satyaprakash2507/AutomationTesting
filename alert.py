import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select #this is used to handle the dropdowns

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Satya"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(5)
alert = driver.switch_to.alert #this will switch the control to the alert

alertText = alert.text
print(alertText)


assert name in alertText

alert.accept() #this will click on the OK button of the alert
#alert.dismiss() #this will click on the Cancel button of the alert