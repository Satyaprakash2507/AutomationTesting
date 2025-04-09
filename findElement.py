import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select #this is used to handle the dropdowns

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")



driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a") #this will return the list of all the countries
print(len(countries))

#for loop to iterate through the list of countries
for country in countries:
    if country.text == "India": #if the country is India then click on it
        country.click()
        break

#driver.find_element(By.ID,"autosuggest").text #this will return the text of the selected country but in this case it will not return the Selected  Text as it is not loaded before.


#print(driver.find_element(By.ID,"autosuggest").get_attribute("value")) #this will return the Selected Text as typed in the textbox


assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India" #this line will check if the selected country is India