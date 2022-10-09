import pytest
from ui.locators import basic_locators
from login import auth
from wait import wait
import time


@pytest.mark.UI
class TestUi:
    def test_login(self, browser):
        auth(browser)
        element = browser.find_element(*basic_locators.HTML)
        assert element.get_attribute('data-ga-username') == 'testgdhdhsjsjs@gmail.com'

    def test_edit_contact_information(self, browser):
        auth(browser)
        browser.get('https://target-sandbox.my.com/profile/contacts')
        elements = browser.find_elements(*basic_locators.EDIT_INF_INPUT)
        elements[0].clear()
        elements[0].send_keys('Kostya Ivanov Sergeevich')
        elements[1].clear()
        elements[1].send_keys('241421414121')
        elements[2].clear()
        elements[2].send_keys('+79193213111')
        element = browser.find_element(*basic_locators.EDIT_INF_BUTTON)
        element.click()
        wait(browser, basic_locators.EDIT_INF_SUCCESS, method='is_displayed')
        element = browser.find_element(*basic_locators.EDIT_INF_SUCCESS)
        assert element.is_displayed()

    @pytest.mark.parametrize(['numbers_elements', 'selector'], [(0, basic_locators.DASHBOARD),
                                                                (1, basic_locators.SEGMENTS),
                                                                (2, basic_locators.BILLING),
                                                                (3, basic_locators.STATISTICS),
                                                                (4, basic_locators.PRO),
                                                                (5, basic_locators.PROFILE),
                                                                (6, basic_locators.TOOLS),
                                                                (7, basic_locators.HELP)])
    def test_elements_on_headers(self, browser, numbers_elements, selector):
        auth(browser)
        wait(browser, basic_locators.ELEMENTS_ON_HEADERS, method='len')
        elements = browser.find_elements(*basic_locators.ELEMENTS_ON_HEADERS)
        elements[numbers_elements].click()
        if numbers_elements == 7:
            browser.switch_to.window(browser.window_handles[1])
        wait(browser, selector, method='is_displayed')
        element = browser.find_element(*selector)
        assert element.is_displayed()

    def test_logout(self, browser):
        auth(browser)
        element = browser.find_element(*basic_locators.LOG_OUT_BUTTON)
        element.click()
        time.sleep(0.5)
        element = browser.find_element(*basic_locators.LOG_OUT_BUTTON_CLICK)
        element.click()
        element = browser.find_element(*basic_locators.HTML)
        assert element.get_attribute('data-ga-userid') == ''

    @pytest.mark.parametrize(['email', 'password'], [('testgd hdhsjsj', 'asasda33333'),
                                                     ('12312414a', 'sadsadsad')])
    def test_negative_auth(self, browser, email, password):
        auth(browser, email=email, password=password)
        wait(browser, basic_locators.NOTIFY_AUTH_FORM, method='is_displayed')
        element = browser.find_element(*basic_locators.NOTIFY_AUTH_FORM)
        assert element.is_displayed()

    @pytest.mark.parametrize(['email', 'password'], [('', 'asasda33333'),
                                                     ('12312414a', ''),
                                                     ('', '')])
    def test_negative_auth_empty_input(self, browser, email, password):
        auth(browser, email=email, password=password)
        browser.find_element(*basic_locators.DISABLE_BUTTON)
