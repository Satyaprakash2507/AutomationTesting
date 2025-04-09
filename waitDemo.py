import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
acutalList = []
driver = webdriver.Chrome()

#implicit wait
driver.implicitly_wait(5) #this will wait for 5 seconds before throwing an exception and it is a global wait
#5 seconds is the maximum time it will wait for the element to be displayed
#as soon as the element is displayed it will move to the next line of code
#disadvantage of implicit wait is that it will wait for the maximum time even if the element is displayed before that time period

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
#to print the number of products displayed
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(results))
assert len(results) > 0

#chaining of xpath to find the product name and click on the Add to cart button

for result in results:
    acutalList.append(result.find_element(By.XPATH,"h4").text) #this will return the name of the product
    result.find_element(By.XPATH,"div/button").click() #this will click on add to cart button of all the products

assert expectedList == acutalList #this line will check if the expected list is equal to the actual list

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click() #this will click on the cart icon
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click() #this will click on the proceed to checkout button

#sum validation
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(4) p") #this will return the list of all the prices of the products in the cart
sum = 0
for price in prices:
    sum = sum + int(price.text) #this will convert the price to integer and add it to the sum

print(sum)

totalAmount = driver.find_element(By.CSS_SELECTOR,".totAmt")

assert sum == int(totalAmount.text) #this line will check if the sum of the prices is equal to the total amount


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy") #this will enter the promo code
driver.find_element(By.CSS_SELECTOR,".promoBtn").click() #this will click on the apply button

#explicit wait by using WebDriverWait and wait is a object of WebDriverWait
#explicit wait is used to wait for a particular element to be displayed, once the element is displayed it will move to the next line of code
wait = WebDriverWait(driver, 10) #this will wait for 10 seconds before throwing an exception
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))#this will wait for the promo info to be 

print(driver.find_element(By.CLASS_NAME,"promoInfo").text) #this will print the promo info  

discountedAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text) #this will return the discount amount

assert int(totalAmount.text) > discountedAmount #this line will check if the total amount is greater than the discounted amount





























