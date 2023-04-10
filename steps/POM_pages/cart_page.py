# Import Seleniums By module
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
import logging
class CartPage(PageFactory):
    # Initialize the CartPage object
    def __init__(self, driver):
        self.driver = driver # Reference the driver

    logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    locators = {
        'cart_button' : ('XPATH', "//div[@class='shop-menu pull-right']/descendant::a[@href='/view_cart']"),
        'checkout_button' : ('XPATH', "//a[@class='btn btn-default check_out']"),
        'login_button' : ('XPATH', "//div[@class='login-form']/descendant::button"),
        'login_page_button' : ('XPATH', "//a[@href='/login']")
    }

    # Function to click the cart button
    def click_cart_button(self):
        self.cart_button.click()
        logging.info('Clicked the %s Button', self.cart_button.text)
    
    # Function to delete a product from the cart given the product ID
    def delete_product(self, product_id):
        # Locate the delete product item button
        delete_product = self.driver.find_element(
            By.XPATH, "//div[@class='table-responsive cart_info']/descendant::a[@data-product-id='{}']".format(product_id))
        delete_product.click() # Click the Delete button
        logging.info('Successfully deleted product with Product ID: %s from the Cart', product_id)  
    # Function to click the checkout button
    def click_checkout_button(self):
        # Locate the checkout item button
        self.checkout_button.click() 
        logging.info('Clicked the %s Button', self.checkout_button.text)


