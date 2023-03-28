from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://automationexercise.com/')

@when('I click on the "{button_name}" button')
def step_impl(context, button_name):
    button = context.driver.find_element(by=By.XPATH, value = "//a[@href='/products']")
    button.click()


@when('I search for "{search_term}"')
def step_impl(context, search_term):
    search_box = context.driver.find_element(by=By.XPATH, value = "//input[@name='search']")
    form = search_box.find_element(by=By.XPATH, value = "//form")
    search_box.send_keys(search_term)
    form.submit()
    button = context.driver.find_element(by=By.XPATH, value="//button[@id='submit_search']")
    button.click()


@then('I should see a list of tshirts')
def step_impl(context):
    tshirts = context.driver.find_element(by=By.XPATH, value = "//p[contains(text(), 'T-Shirt')]")
    assert len(tshirts) > 0
    context.driver.quit()
