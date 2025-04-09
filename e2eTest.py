import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR," a[href*='shop']").click() #this will click on the shop link

products = driver.find_elements(By.XPATH,"//div[@class='card h-100']") #this will return the list of all the products displayed on the page

for product in products:
    product_name = product.find_element(By.XPATH,"div/h4/a").text #this will return the name of the product
    if product_name == "Blackberry":
        product.find_element(By.XPATH,"div/button").click() #this will click on the add to cart button of the Blackberry product


driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click() #this will click on the cart button

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click() #this will click on the checkout button
driver.find_element(By.ID,"country").send_keys("Ind") #this will enter the country name in the country field

wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"India"))) #this will wait for the India link to be displayed
driver.find_element(By.LINK_TEXT,"India").click() #this will click on the India link
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click() #this will click on the checkbox
driver.find_element(By.XPATH,"//input[@type='submit']").click() 
successText = driver.find_element(By.CLASS_NAME,"alert-success").text 
assert "Success! Thank you!" in successText 