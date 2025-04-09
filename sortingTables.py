import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
browserSortedVeggies = []
driver = webdriver.Chrome()

#implicit wait
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header to sort the table
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#collect all the veggies name -> BrowserSoretedVeggiesList (B ,A , C)
veggieWebElement = driver.find_elements(By.XPATH, "//tr/td[1]") 
for element in veggieWebElement:
    browserSortedVeggies.append(element.text)

originalBrowserSortedList = browserSortedVeggies.copy()
#sort this browserSortedVeggiesList -> newSortedVeggiesList (A , B , C)
browserSortedVeggies.sort()
#sort this browserSortedVeggiesList -> newSortedVeggiesList
assert browserSortedVeggies == originalBrowserSortedList