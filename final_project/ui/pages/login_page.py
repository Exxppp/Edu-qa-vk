from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginPageLocators


class LoginPage(BasePage):

    locators = LoginPageLocators
    url = 'http://localhost:9090/'

    def login(self, username, password):
        self.input_text(self.locators.INPUT_USERNAME, username)
        self.input_text(self.locators.INPUT_PASSWORD, password)
        self.click(self.locators.BUTTON_LOGIN)
