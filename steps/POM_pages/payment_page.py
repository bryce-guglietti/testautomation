# Import the selenium By Module 
from selenium.webdriver.common.by import By

class PaymentPage:
    # Initialize the PaymentPage object
    def __init__(self, driver):
        self.driver = driver
        # Locate the confirm button with XPath
        self.confirm_button = self.driver.find_element(by=By.XPATH, value ="//form[@id='payment-form']/descendant::button")
    
    # Function to click the confirm button
    def click_confirm_button(self):
        self.confirm_button.click()

    # Function to fill the paymennt info form with name, number, cvc, expiry month, and expiry year
    def fill_payment_info(self, name, number, cvc, expiry_month, expiry_year):
        # Locate the name field with XPath and fill it with the parameter
        name_field = self.driver.find_element(by=By.XPATH, value = "//form[@id='payment-form']/descendant::input[@name='name_on_card']")
        name_field.send_keys(name)

        # Locate the number field with XPath and fill it with the parameter
        number_field = self.driver.find_element(by=By.XPATH, value = "//form[@id='payment-form']/descendant::input[@name='card_number']")
        number_field.send_keys(number)

        # Locate the cvc field with XPath and fill it with the parameter
        cvc_field = self.driver.find_element(by=By.XPATH, value = "//form[@id='payment-form']/descendant::input[@name='cvc']")
        cvc_field.send_keys(cvc)

        # Locate the expiry month field with XPath and fill it with the parameter
        exp_field = self.driver.find_element(by=By.XPATH, value = "//form[@id='payment-form']/descendant::input[@name='expiry_month']")
        exp_field.send_keys(expiry_month)

        # Locate the expiry year field with XPath and fill it with the parameter
        exp_year_field = self.driver.find_element(by=By.XPATH, value = "//form[@id='payment-form']/descendant::input[@name='expiry_year']")
        exp_year_field.send_keys(expiry_year)
