from seleniumpagefactory.Pagefactory import PageFactory
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

    # Function to click the login button
    def click_login_button(self):
        self.login_page_button.click()

    # Function to login the user with the Email and Password
    def login_to_user(self, email, password):
        # Find the email field and fill it with the passed perameter
        self.email_field.set_text(email)

        # Find the password field and fill it with the passed peramater
        self.password_field.set_text(password)

        # Find the Login Button and click it
        self.login_button.click()
