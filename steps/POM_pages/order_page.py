# Import the Selenium By module
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
import logging

class OrderPage(PageFactory):
    # Initialize the OrderPage object
    def __init__(self, driver):
        self.driver = driver
        
    #Import Logging
    logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    #Set up locators for Order Page
    locators = {
        'checkout_button' : ('XPATH', "//a[@class='btn btn-default check_out']")
    }
    # Function to click the Place Order Button
    def click_place_order(self):
        self.checkout_button.click()
        logging.info('Clicked the Checkout Button')
