import pytest
from selenium import webdriver

#to run this test file, run the following command in the terminal: python -m pytest test_e2eFrameworkTest.py --browser_name Chrome

#this is anecessary step to add the command line option to pytest, 
def pytest_addoption(parser): 
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection") 

@pytest.fixture(scope="function")
def browserInstance(request): #the request object is used to get the command line options passed to pytest
    browser_name = request.config.getoption("browser_name") #--browser Chrome is the command line option passed to pytest,it take the name from the command line
    if browser_name == "Chrome":
        driver = webdriver.Chrome()
        
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/") #this will open the url in the browser
    yield driver # This will return the driver instance to the test function,will run before test function execution
    driver.close() # This will close the browser after the test is completed