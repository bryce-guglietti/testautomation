# Import behave and selenium
from behave import given, when, then
from selenium import webdriver
<<<<<<< HEAD

# Import the POM classes
from POM_pages.login_page import LoginPage
from POM_pages.product_page import ProductPage
from POM_pages.cart_page import CartPage
from POM_pages.order_page import OrderPage
from POM_pages.payment_page import PaymentPage
from POM_pages.invoice_page import InvoicePage
=======
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_button = self.driver.find_element(by=By.XPATH, value = "//a[@href='/login']")
    
    def click_login_button(self):
        self.login_button.click()

    def login_to_user(self, email, password):
        email_field = self.driver.find_element(by=By.XPATH, value = "//form['/login']/input[@type='email']")
        email_field.send_keys(email)

        password_field = self.driver.find_element(by=By.XPATH, value = "//form['/login']/input[@type='password']")
        password_field.send_keys(password)

        password_field.submit()

        self.driver.find_element(by=By.XPATH, value ="//form['/login']").click()

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_button = self.driver.find_element(by=By.XPATH, value = "//a[@href='/products']")

    def click_product_button(self):
        self.product_button.click()

    def search_for_product(self, product):
        search_box = self.driver.find_element(by=By.XPATH, value = "//input[@name='search']")
        form = search_box.find_element(by=By.XPATH, value = "//form")

        search_box.send_keys(product)
        form.submit()

        button = self.driver.find_element(by=By.XPATH, value="//button[@id='submit_search']")
        button.click()

    def add_product_to_cart(self, product_id):
        add_button = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='single-products']/*/*[@data-product-id='{}']".format(product_id))))
        add_button.click()

        cont_shopping_button = WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='modal-footer']/descendant::button")))
        cont_shopping_button.click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = self.driver.find_element(by=By.XPATH, value = "//a[@href='/view_cart']")

    def click_cart_button(self):
        self.cart_button.click()
>>>>>>> efd72d77a1aec2375410546ccb6c3e78c4b0bb41

# Start the webdriver with the ad blocker active
@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.install_addon(r"C:\cp476\uBlock0_1.48.5b2.firefox.signed.xpi", temporary=True)
    context.driver.get('https://automationexercise.com/')

<<<<<<< HEAD
# Call the LoginPage and call the login button
=======
>>>>>>> efd72d77a1aec2375410546ccb6c3e78c4b0bb41
@when('I click on the login button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()

<<<<<<< HEAD
# Call the LoginPage and the Login to user function
@when('I login to my account')
def step_impl(context):
    login_page = LoginPage(context.driver)
    # The parameters are Username and Password
    login_page.login_to_user('Bryce81@outlook.com', '123')

# Call the ProductPage and click the product button
=======
@when('I login to my account')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.login_to_user('Bryce81@outlook.com', '123')

>>>>>>> efd72d77a1aec2375410546ccb6c3e78c4b0bb41
@when('I click on the "{button_name}" button')
def step_impl(context, button_name):
    product_page = ProductPage(context.driver)
    product_page.click_product_button()

# Call the ProductPage and Search for a Product
@when('I search for "{search_term}"')
def step_impl(context, search_term):
    product_page = ProductPage(context.driver)
    product_page.search_for_product(search_term)

<<<<<<< HEAD
# Call the ProductPage and add 2 Products to Cart
@when('I add 2 "{search_term}" to cart')
def step_impl(context, search_term):
    product_page = ProductPage(context.driver)

    # The parameter is the product ID's 
    product_page.add_product_to_cart('2')
    product_page.add_product_to_cart('28')

# Call the CartPage and Click the Cart Button
@when('I click on the Cart button')
def step_impl(context):
    cart_page = CartPage(context.driver)
    cart_page.click_cart_button()

# Call the CartPage and call the delete product fucntion
@when('I delete an item')
def step_impl(context):
    cart_page = CartPage(context.driver)
    # The parameter is the Product ID
    cart_page.delete_product('28')

# Call the CartPage and click the Checkout Button
@when('I click on the Checkout button')
def step_impl(context):
    cart_page = CartPage(context.driver)
    cart_page.click_checkout_button()

# Call the OrderPage and click the Place Order Button
@when('I click on the Place Order button')
def step_impl(context):
    order_page = OrderPage(context.driver)
    order_page.click_place_order()

# Call the PaymentPage and Fill out the Credit Card Form
@when('I fill out the credit card form')
def step_impl(context):
    payment_page = PaymentPage(context.driver)
    # The Parameters are Name, Credit Card Number, CVC, Expiry Month, and Expiry Year
    payment_page.fill_payment_info('John Doe', '1234123412341234', '123', '10', '2025')
    payment_page.click_confirm_button()

# Call the InvoicePage and click the invoice page
@then('I click on the invoice button')
def step_impl(context):
    invoice_page = InvoicePage(context.driver)
    invoice_page.click_download_invoice()
    # Tear Down the WebDriver
    context.driver.quit()
=======
@when('I add 2 T-Shirts to cart')
def step_impl(context):
        product_page = ProductPage(context.driver)
        product_page.add_product_to_cart('2')

        product_page.add_product_to_cart('28')

@when('I click on the Cart button')
def step_impl(context):
    cart_page = CartPage(context.driver)
    cart_page.click_cart_button()

@when('I delete an item')
def step_impl(context):
   tr_element = context.driver.find_element(By.XPATH, "//*[@class='cart_delete']")

   tr_element.click()

@when('I click on the Checkout button')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-default check_out']"))).click()

@when('I click on the Place Order button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='btn btn-default check_out']").click()

@when('I fill out the credit card form')
def step_impl(context):
    name_field = context.driver.find_element(by=By.XPATH, value = "//form[@id='payment-form']/*/*/input[@name='name_on_card']")
    name_field.send_keys('Bryce Guglietti')

    number_field = context.driver.find_element(by=By.XPATH, value = "//form[@id='payment-form']/*/*/input[@name='card_number']")
    number_field.send_keys('1234432112344321')

    cvc_field = context.driver.find_element(by=By.XPATH, value = "//form[@id='payment-form']/*/*/input[@name='cvc']")
    cvc_field.send_keys('999')

    exp_field = context.driver.find_element(by=By.XPATH, value = "//form[@id='payment-form']/*/*/input[@name='expiry_month']")
    exp_field.send_keys('12')

    exp_year_field = context.driver.find_element(by=By.XPATH, value = "//form[@id='payment-form']/*/*/input[@name='expiry_year']")
    exp_year_field.send_keys('2099')


    context.driver.find_element(by=By.XPATH, value ="//button[@id='submit']").click()

@then('I click on the invoice button')
def step_impl(context):
   invoice = context.driver.find_element(By.XPATH, "//a[@class='btn btn-default check_out']")

   invoice.click()
>>>>>>> efd72d77a1aec2375410546ccb6c3e78c4b0bb41
