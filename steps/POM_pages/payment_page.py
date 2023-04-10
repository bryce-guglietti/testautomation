# Import the selenium By Module 
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
import logging
class PaymentPage(PageFactory):
    # Initialize the PaymentPage object
    def __init__(self, driver):
        self.driver = driver

    logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    locators = {
        'confirm_button' : ('XPATH',"//form[@id='payment-form']/descendant::button"),
        'name_field' : ('XPATH',"//form[@id='payment-form']/descendant::input[@name='name_on_card']"),
        'number_field' : ('XPATH',"//form[@id='payment-form']/descendant::input[@name='card_number']"),
        'cvc_field' : ('XPATH',"//form[@id='payment-form']/descendant::input[@name='cvc']"),
        'exp_month_field' : ('XPATH',"//form[@id='payment-form']/descendant::input[@name='expiry_month']"),
        'exp_year_field' : ('XPATH',"//form[@id='payment-form']/descendant::input[@name='expiry_year']"),
    }

    # Function to click the confirm button
    def click_confirm_button(self):
        self.confirm_button.click()
        logging.info('Successfully Confirmed Purchase')

    # Function to fill the paymennt info form with name, number, cvc, expiry month, and expiry year
    def fill_payment_info(self, name, number, cvc, expiry_month, expiry_year):
        # Locate the name field with XPath and fill it with the parameter
        self.name_field.set_text(name)
        logging.info('Filled the Name Field with the Term: %s', name)
        self.number_field.set_text(number)
        logging.info('Filled the Number Field with the Term: %s', number)
        self.cvc_field.set_text(cvc)
        logging.info('Filled the CVC Field with the Term: %s', cvc)
        self.exp_month_field.set_text(expiry_month)
        logging.info('Filled the Expiry Month Field with the Term: %s', expiry_month)
        self.exp_year_field.set_text(expiry_year)
        logging.info('Filled the Expiry Year Field with the Term: %s', expiry_year)
