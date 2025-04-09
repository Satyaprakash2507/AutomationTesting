import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") #this will start the browser in maximized mode
chrome_options.add_argument("--disable-infobars") #this will disable the infobars
chrome_options.add_argument("--headless") #this will run the browser in headless mode (without GUI)
chrome_options.add_argument("--ignore-certificate-errors") #this will ignore the certificate errors
driver = webdriver.Chrome(options=chrome_options) #this will create a new instance of the Chrome browser

#implicit wait
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

print(driver.title) #this will print the title of the page