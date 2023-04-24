# Import selenium's By module
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
import logging
class InvoicePage(PageFactory):
    # Initialize the InvoicePage
    def __init__(self, driver):
        self.driver = driver

    #Set up logging
    logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    #Set up Locators for Invoice Page
    locators = {
        'invoice_button' : ('XPATH', "//a[@class='btn btn-default check_out']"),
    }
    # Function to click to dowload invoice button
    def click_download_invoice(self):
        self.invoice_button.click()
        if "#google_vignette" in self.driver.current_url:
            self.driver.back()
            self.invoice_button.click()
        logging.info('Clicked the %s Button', self.invoice_button.text)
