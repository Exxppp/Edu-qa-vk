from ui.locators.basic_locators import LoginPageLocators
from ui.pages.base_page import BasePage
from ui.pages.dashboard_page import DashboardPage
import allure


class LoginPage(BasePage):

    @allure.step('auth')
    def login(self, email='testgdhdhsjsjs@gmail.com', password='123456q'):
        self.driver.get('https://target-sandbox.my.com/')
        self.click(LoginPageLocators.LOG_IN_BUTTON)
        self.input_text(LoginPageLocators.INPUT_EMAIL, email)
        self.input_text(LoginPageLocators.INPUT_PASSWORD, password)
        self.click(LoginPageLocators.LOG_IN_BUTTON_AUTH_FORM)
        return DashboardPage(self.driver)
