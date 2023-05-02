from seleniumpagefactory.Pagefactory import PageFactory
import logging
class LoginPage(PageFactory):
    # Initialize the LoginPage
    def __init__(self, driver):
        self.driver = driver

    #Set up logging
    logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    #Set up the locators for the Login Page
    locators = {
        'email_field' : ('XPATH', "//div[@class='login-form']/descendant::input[@type='email']"),
        'password_field' : ('XPATH', "//div[@class='login-form']/descendant::input[@type='password']"),
        'login_button' : ('XPATH ', "//div[@class='login-form']/descendant::button"),
        'login_page_button' : ('XPATH', "//a[@href='/login']")
    }

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
        if "#google_vignette" in self.driver.current_url:
            self.driver.back()
            self.login_button.click()

        logging.info('Completed Login')
