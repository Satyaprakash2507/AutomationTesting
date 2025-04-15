from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browserutils import BrowserUtils  


class Checkout_Confirmation(BrowserUtils):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver) # this will call the constructor of the parent class and initialize the driver in the parent class.

        
        self.checkout_button = (By.XPATH,"//button[@class='btn btn-success']")
        self.county_input = (By.ID,"country")
        self.coutry_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.XPATH,"//input[@type='submit']")
        self.success_message = (By.CLASS_NAME,"alert-success")

    def checkout(self):
         self.driver.find_element(*self.checkout_button).click()
        

    def enter_delivery_address(self, countryName):
        self.driver.find_element(*self.county_input).send_keys(countryName) 
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_element_located(self.coutry_option)) 
        self.driver.find_element(*self.coutry_option).click() 
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click() 
        successText = self.driver.find_element(*self.success_message).text 

    def validate_order(self):
        successText = self.driver.find_element(*self.success_message).text 
        assert "Success! Thank you!" in successText
