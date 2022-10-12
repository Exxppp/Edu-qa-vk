import pytest
from ui.locators import basic_locators
import time


class BaseCase:
    browser = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.browser = browser

    def auth(self, email='testgdhdhsjsjs@gmail.com', password='123456q'):
        self.browser.get('https://target-sandbox.my.com/')
        self.click(basic_locators.LOG_IN_BUTTON)
        self.input_text(email, basic_locators.INPUT_EMAIL)
        self.input_text(password, basic_locators.INPUT_PASSWORD)
        self.click(basic_locators.LOG_IN_BUTTON_AUTH_FORM)

    def find(self, by, what):
        return self.browser.find_element(by, what)

    def input_text(self, query, locator):
        search = self.find(*locator)
        search.clear()
        search.send_keys(query)

    def click(self, locator):
        element = self.find(*locator)
        element.click()

    def click_in_array(self, locator, number_element):
        element = self.browser.find_elements(*locator)
        element[number_element].click()

    def logout(self):
        self.click(basic_locators.LOG_OUT_BUTTON)
        time.sleep(0.5)
        self.click(basic_locators.LOG_OUT_BUTTON_CLICK)

    def wait(self, selector, method='len', sec=8, length=8):
        times = sec * 5
        if method == 'len':
            for i in range(times):
                if len(self.browser.find_elements(*selector)) == length:
                    return True
                else:
                    time.sleep(0.2)
        elif method == 'is_displayed':
            for i in range(times):
                element = self.browser.find_element(*selector)
                if element:
                    if element.is_displayed():
                        return True
                    else:
                        time.sleep(0.2)
                else:
                    time.sleep(0.2)
        return False
