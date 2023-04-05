# Import Seleniums By, WebDriverWait, and expected_conditions modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from seleniumpagefactory.Pagefactory import PageFactory


class ProductPage(PageFactory):
    # Initialize the ProductPage object
    def __init__(self, driver):
        self.driver = driver


    locators = {
        'search_form' : ('XPATH', "//div[@class='container']/descendant::input[@class='form-control input-lg']"),
        'search_button' : ('XPATH', "//button[@id='submit_search']"),
        'product_page_button' : ('XPATH', "//a[@href='/products']"),
        'add_product_button' : ('XPATH', f"//div[@class='productinfo text-center']/descendant::a[@data-product-id='{product_id}']")
    }

    # Function to click the product page button
    def click_product_button(self):
        self.product_page_button.click()

    # Function to search for products using a product search parameter 
    def search_for_product(self, product):
        # Locate the search box and form using XPath
        self.search_form.set_text(product)

        self.search_button.click()

    # Function to add a product to the cart using the product id parameter 
    def add_product_to_cart(self, product_id):
        # Locate the add button using XPath and parameter and wait for it to be clickable using WebDriverWait
        # add_button = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, "//div[@class='productinfo text-center']/descendant::a[@data-product-id='{}']".format(product_id))))
        # add_button.click()
        self.add_product_button.click()

        # Locate the Continue Shopping Button with XPath and wait for it to be clickable 
        cont_shopping_button = WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='modal-footer']/descendant::button")))
        cont_shopping_button.click()
