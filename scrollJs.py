from selenium import webdriver
from selenium.webdriver.common.by import By
import time



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless") #this will run the browser in headless mode, headless mode is used to run the browser in the background without opening the browser window
chrome_options.add_argument("--ignore-certificate-errors") #this will ignore the certificate errors

driver = webdriver.Chrome(options=chrome_options)  #this will open the browser in headless mode


#implicit wait
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(5) 

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #this will scroll to the bottom of the page
driver.get_screenshot_as_file("screenshot.png") #this will take a screenshot of the page and save it as screenshot.png
time.sleep(5) 