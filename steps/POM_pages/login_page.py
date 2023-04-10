from seleniumpagefactory.Pagefactory import PageFactory
import logging
class LoginPage(PageFactory):
    # Initialize the LoginPage
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'email_field' : ('XPATH', "//div[@class='login-form']/descendant::input[@type='email']"),
        'password_field' : ('XPATH', "//div[@class='login-form']/descendant::input[@type='password']"),
        'login_button' : ('XPATH', "//div[@class='login-form']/descendant::button"),
        'login_page_button' : ('XPATH', "//a[@href='/login']")
    }
    logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    # Function to click the login button
    def click_login_button(self):
        self.login_page_button.click()
        logging.info('Clicked on the %s Button', self.login_page_button.text)

    # Function to login the user with the Email and Password
    def login_to_user(self, email, password):
        # Find the email field and fill it with the passed perameter
        self.email_field.set_text(email)
        logging.info('Set the text for the %s field', self.email_field.get_attribute('name'))
        # Find the password field and fill it with the passed peramater
        self.password_field.set_text(password)
        logging.info('Set the text for the %s field', self.password_field.get_attribute('name'))
        # Find the Login Button and click it
        self.login_button.click()
        logging.info('Completed Login')
