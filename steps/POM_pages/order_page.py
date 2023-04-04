# Import the Selenium By module
from selenium.webdriver.common.by import By

class OrderPage:
    # Initialize the OrderPage object
    def __init__(self, driver):
        self.driver = driver
        # Locate the place order button using XPath
        self.place_order_button = self.driver.find_element(By.XPATH, "//a[@class='btn btn-default check_out']")

    # Function to click the Place Order Button
    def click_place_order(self):
        self.place_order_button.click()
