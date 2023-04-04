# Import seleniums By Module
from selenium.webdriver.common.by import By

class LoginPage:
    # Initialize the LoginPage
    def __init__(self, driver):
        self.driver = driver
        # Locate the login button using XPath
        self.login_button = self.driver.find_element(by=By.XPATH, value = "//a[@href='/login']")
    
    # Function to click the login button
    def click_login_button(self):
        self.login_button.click()

    # Function to login the user with the Email and Password
    def login_to_user(self, email, password):
        # Find the email field and fill it with the passed perameter
        email_field = self.driver.find_element(by=By.XPATH, value = "//form['/login']/input[@type='email']")
        email_field.send_keys(email)

        # Find the password field and fill it with the passed peramater
        password_field = self.driver.find_element(by=By.XPATH, value = "//form['/login']/input[@type='password']")
        password_field.send_keys(password)

        password_field.submit() # Submit the field

        # Find the Login Button and click it
        self.driver.find_element(by=By.XPATH, value ="//form['/login']").click()
