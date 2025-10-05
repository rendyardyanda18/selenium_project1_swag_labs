from locators.login_locators import LoginLocators
from utils.config import Config

class LoginPage:
    def __init__(self, driverconftest):
        self.browser = driverconftest
        self.url = Config.URL_MAINPAGE

    def open(self):
        self.browser.get(self.url)

    def login(self, username, password):
        self.browser.find_element(*LoginLocators.USERNAME).send_keys(username)
        self.browser.find_element(*LoginLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*LoginLocators.ERROR_MSG).text

