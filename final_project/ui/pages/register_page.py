from ui.pages.base_page import BasePage
from ui.locators.basic_locators import RegisterPageLocators
import allure


class RegisterPage(BasePage):

    locators = RegisterPageLocators

    @allure.step('Выполняем регистрацию')
    def register(self, name=None, surname=None, middlename=None, username=None, email=None, password=None,
                 repeat_password=None, checkbox=True):

        self.open()
        self.input_text(self.locators.INPUT_NAME, name)
        self.input_text(self.locators.INPUT_SURNAME, surname)
        self.input_text(self.locators.INPUT_MIDDLENAME, middlename)
        self.input_text(self.locators.INPUT_USERNAME, username)
        self.input_text(self.locators.INPUT_EMAIL, email)
        self.input_text(self.locators.INPUT_PASSWORD, password)
        self.input_text(self.locators.INPUT_REPEAT_PASSWORD, repeat_password)
        if checkbox:
            self.click(self.locators.ACCEPT)
        self.click(self.locators.BUTTON_REG)
