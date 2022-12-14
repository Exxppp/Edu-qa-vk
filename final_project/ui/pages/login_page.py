from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginPageLocators
import allure


class LoginPage(BasePage):

    locators = LoginPageLocators

    @allure.step('Авторизация')
    def login(self, username, password):
        self.open()
        self.input_text(self.locators.INPUT_USERNAME, username)
        self.input_text(self.locators.INPUT_PASSWORD, password)
        self.click(self.locators.BUTTON_LOGIN)

    @allure.step('Предупреждающее сообщение')
    def get_text_from_alert(self):
        text = self.get_text(self.locators.ALERT)

        return text
