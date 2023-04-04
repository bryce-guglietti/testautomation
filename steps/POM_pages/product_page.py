# Import Seleniums By, WebDriverWait, and expected_conditions modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class ProductPage:
    # Initialize the ProductPage object
    def __init__(self, driver):
        self.driver = driver
        #Locate the product button using the XPath
        self.product_button = self.driver.find_element(by=By.XPATH, value = "//a[@href='/products']")

    # Function to click the product page button
    def click_product_button(self):
        self.product_button.click()

    # Function to search for products using a product search parameter 
    def search_for_product(self, product):
        # Locate the search box and form using XPath
        search_box = self.driver.find_element(by=By.XPATH, value = "//input[@name='search']")
        form = search_box.find_element(by=By.XPATH, value = "//form")

        # Send the product search term to the search box
        search_box.send_keys(product)
        form.submit() # submit form

        # Locate the search button using XPath and Click it 
        search_button = self.driver.find_element(by=By.XPATH, value="//button[@id='submit_search']")
        search_button.click()

    # Function to add a product to the cart using the product id parameter 
    def add_product_to_cart(self, product_id):
        # Locate the add button using XPath and parameter and wait for it to be clickable using WebDriverWait
        add_button = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='single-products']/*/*[@data-product-id='{}']".format(product_id))))
        add_button.click()

        # Locate the Continue Shopping Button with XPath and wait for it to be clickable 
        cont_shopping_button = WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='modal-footer']/descendant::button")))
        cont_shopping_button.click()
