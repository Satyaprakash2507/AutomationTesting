import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select #this is used to handle the dropdowns

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

# for loop to iterate through the list of checkboxes and select the checkbox with value option2 ,click on it and check if it is selected 
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break


radioButton = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radioButton[2].click() #this will click on the 3rd radio button
assert radioButton[2].is_selected() #this will check if the 3rd radio button is selected


assert driver.find_element(By.ID,"displayed-text").is_displayed() #this will check if the text box is displayed or not

driver.find_element(By.ID,"hide-textbox").click() #this will hide the text box

assert not driver.find_element(By.ID,"displayed-text").is_displayed() #this will check if the text box is displayed or not