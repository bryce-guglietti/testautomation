from behave import given, when, then
from selenium import webdriver
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

@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.install_addon(r"C:\cp476\uBlock0_1.48.5b2.firefox.signed.xpi", temporary=True)
    context.driver.get('https://automationexercise.com/')

@when('I click on the login button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()

@when('I login to my account')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.login_to_user('Bryce81@outlook.com', '123')

@when('I click on the "{button_name}" button')
def step_impl(context, button_name):
    product_page = ProductPage(context.driver)
    product_page.click_product_button()

@when('I search for "{search_term}"')
def step_impl(context, search_term):
    product_page = ProductPage(context.driver)
    product_page.search_for_product(search_term)

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
