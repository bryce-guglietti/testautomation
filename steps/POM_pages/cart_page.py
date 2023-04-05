# Import Seleniums By module
from selenium.webdriver.common.by import By

class CartPage:
    # Initialize the CartPage object
    def __init__(self, driver):
        self.driver = driver # Reference the driver
        # find the view cart element using XPath
        self.cart_button = self.driver.find_element(
            by=By.XPATH, value = "//div[@class='shop-menu pull-right']/descendant::a[@href='/view_cart']")

    # Function to click the cart button
    def click_cart_button(self):
        self.cart_button.click()
    
    # Function to delete a product from the cart given the product ID
    def delete_product(self, product_id):
        # Locate the delete product item button
        delete_product = self.driver.find_element(
            By.XPATH, "//div[@class='table-responsive cart_info']/descendant::a[@data-product-id='{}']".format(product_id))
        delete_product.click() # Click the Delete button
    
    # Function to click the checkout button
    def click_checkout_button(self):
        # Locate the checkout item button
        self.checkout_button = self.driver.find_element(By.XPATH, "//a[@class='btn btn-default check_out']")
        self.checkout_button.click() # Click the checkout button

