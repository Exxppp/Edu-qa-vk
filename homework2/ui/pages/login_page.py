from ..locators.locators import LoginPageLocators
from .base_page import BasePage
from .main_page import MainPage


class LoginPage(BasePage):

    def login(self, email='testgdhdhsjsjs@gmail.com', password='123456q'):
        self.driver.get('https://target-sandbox.my.com/')
        self.click(LoginPageLocators.LOG_IN_BUTTON)
        self.input_text(LoginPageLocators.INPUT_EMAIL, email)
        self.input_text(LoginPageLocators.INPUT_PASSWORD, password)
        self.click(LoginPageLocators.LOG_IN_BUTTON_AUTH_FORM)
        return MainPage(self.driver)
