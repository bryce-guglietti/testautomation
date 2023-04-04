# Import selenium's By module
from selenium.webdriver.common.by import By

class InvoicePage:
    # Initialize the InvoicePage
    def __init__(self, driver):
        self.driver = driver
        # Locate the download invoice button
        self.download_invoice = self.driver.find_element(
            By.XPATH, "//a[@class='btn btn-default check_out']")

    # Function to click to dowload invoice button
    def click_download_invoice(self):
        self.download_invoice.click()
