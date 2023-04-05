# Import behave and selenium
from behave import given, when, then
from selenium import webdriver

# Import the POM classes
from POM_pages.login_page import LoginPage
from POM_pages.product_page import ProductPage
from POM_pages.cart_page import CartPage
from POM_pages.order_page import OrderPage
from POM_pages.payment_page import PaymentPage
from POM_pages.invoice_page import InvoicePage

from functions.avoid_ads import click_avoid_ads

# Start the webdriver with the ad blocker active
@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.install_addon(r"C:\cp476\uBlock0_1.48.5b2.firefox.signed.xpi", temporary=True)
    context.driver.get('https://automationexercise.com/')

# Call the LoginPage and call the login button
@when('I click on the login button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()

# Call the LoginPage and the Login to user function
@when('I login to my account')
def step_impl(context):
    login_page = LoginPage(context.driver)
    # The parameters are Username and Password
    login_page.login_to_user('Bryce81@outlook.com', '123')

# Call the ProductPage and click the product button
@when('I click on the "{button_name}" button')
def step_impl(context, button_name):
    product_page = ProductPage(context.driver)
    product_page.click_product_button()

# Call the ProductPage and Search for a Product
@when('I search for "{search_term}"')
def step_impl(context, search_term):
    product_page = ProductPage(context.driver)
    product_page.search_for_product(search_term)

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
