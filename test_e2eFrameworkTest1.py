import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from loginObject.login import LoginPage
from loginObject.shopPage import ShopPage
from loginObject.checkout_comfi import Checkout_Confirmation
import json

test_data_path = r'C:\Users\yaduv\Desktop\SelwithPy\loginObject\data\test_e2eFrameworkTest1.json' #path to the test data file
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"] #this will load the test data from the json file and entire value is retrivied


@pytest.mark.usefixtures("browserInstance") 
@pytest.mark.parametrize("test_list_items", test_list) #to use test_data in the function we need to do like this test_list extrac all the values and push it into the test_list_items
def test_e2e(browserInstance,test_list_items):
    driver = browserInstance #this is comin from conftest.py file, Yield driver line
    

    loginPage = LoginPage(driver) #this will create an instance of the LoginPage class and sending driver as an argument to the Login constructor
    print(loginPage.getTitle()) #this will call the getTitle method of the BrowserUtils class and return the title of the page
    shop_page = loginPage.login(test_list_items["userEmail"], test_list_items["userPassword"]) #this will call the login method of the LoginPage class
    
   
   # shop_page = ShopPage(driver) #creating the object of the class. Instend of here i will create the object in the Login.py file
    shop_page.addProduct_to_cart(test_list_items["productName"])
    print(shop_page.getTitle())
    
    checkout_confirmation =  shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()

    

  