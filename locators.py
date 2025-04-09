import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select #this is used to handle the dropdowns

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

#Xpath, Id, Name, CssSelector, LinkText, PartialLinkText, TagName, Classname are the ways to identify the elements in the webpage

driver.find_element(By.NAME,"email").send_keys("satya@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys(123456)
driver.find_element(By.ID,"exampleCheck1").click()

#CSS Selector Syntax:- tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Satya")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

#static dropdown 
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1")) #here dropdown is an object of Select class
# dropdown.select_by_index(1) #selecting the option by index
dropdown.select_by_visible_text("Female") #selecting the option by visible text
# dropdown.select_by_value("M") #selecting the option by value

# Xpath Syntax:- //tagname[@attribute='value']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

assert "Success" in message #this line will check if the message contains the word success

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("India")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()


time.sleep(10)