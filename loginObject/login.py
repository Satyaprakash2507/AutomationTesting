   
from utils.browserutils import BrowserUtils  

from selenium.webdriver.common.by import By

from loginObject.shopPage import ShopPage
#self is a instance of class variable. it is used to use the class variable in the class methods
class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver) # this will call the constructor of the parent class and initialize the driver in the parent class.
        self.driver = driver

        self.username_input = (By.ID,"username") # this is a tuple (By.ID,"username") 
        self.password = (By.NAME,"password")
        self.sign_button = (By.ID,"signInBtn")


    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username) # * is used to that the 2 argument otherwise it would have only one. 
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click() 

        shop_page = ShopPage(self.driver)# creating the object of the class. as the login page take us to the shop page directly so its better to create the objects here
        return shop_page