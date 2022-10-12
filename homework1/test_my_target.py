import pytest
from selenium.webdriver.common.by import By
from login import auth
from wait import wait
import time


@pytest.mark.UI
class TestUi:
    def test_login(self, browser):
        auth(browser)
        element = browser.find_element(By.CSS_SELECTOR, 'html')
        assert element.get_attribute('data-ga-username') == 'testgdhdhsjsjs@gmail.com'

    def test_edit_contact_information(self, browser):
        auth(browser)
        browser.get('https://target-sandbox.my.com/profile/contacts')
        elements = browser.find_elements(By.CSS_SELECTOR, '.input__inp.js-form-element')
        elements[0].clear()
        elements[0].send_keys('Kostya Ivanov Sergeevich')
        elements[1].clear()
        elements[1].send_keys('241421414121')
        elements[2].clear()
        elements[2].send_keys('+79193213111')
        element = browser.find_element(By.CSS_SELECTOR, '.button')
        element.click()
        wait(browser, '.js-group-form-success-bg', method='is_displayed')
        element = browser.find_element(By.CSS_SELECTOR, '.js-group-form-success-bg')
        assert element.is_displayed()

    @pytest.mark.parametrize(['numbers_elements', 'selector'], [(0, 'li.instruction-module-item-1geUDm:nth-child(4)'),
                                                                (1, '.page_segments_segmentslist'),
                                                                (2, '.current-page_billing'),
                                                                (3, '.page_statistics_summary_nt'),
                                                                (4, '.current-page_no-type'),
                                                                (5, '.page_profile'),
                                                                (6, '.page_tools'),
                                                                (7, '#allrecords')])
    def test_elements_on_headers(self, browser, numbers_elements, selector):
        auth(browser)
        wait(browser, selector='.center-module-buttonWrap-1dlSMH', method='len')
        elements = browser.find_elements(By.CSS_SELECTOR, '.center-module-buttonWrap-1dlSMH')
        elements[numbers_elements].click()
        if numbers_elements == 7:
            browser.switch_to.window(browser.window_handles[1])
        wait(browser, selector, method='is_displayed')
        element = browser.find_element(By.CSS_SELECTOR, selector)
        assert element.is_displayed()

    def test_logout(self, browser):
        auth(browser)
        element = browser.find_element(By.CSS_SELECTOR, '.right-module-mail-aXwV1G')
        element.click()
        time.sleep(0.5)
        element = browser.find_element(By.CSS_SELECTOR, 'li.rightMenu-module-rightMenuItem-1TjQzn:nth-child(2)')
        element.click()
        element = browser.find_element(By.CSS_SELECTOR, 'html')
        assert element.get_attribute('data-ga-userid') == ''

    @pytest.mark.parametrize(['email', 'password'], [('testgd hdhsjsj', 'asasda33333'),
                                                     ('12312414a', 'sadsadsad')])
    def test_negative_auth(self, browser, email, password):
        auth(browser, email=email, password=password)
        wait(browser, '.notify-module-error-17z7Pp', method='is_displayed')
        element = browser.find_element(By.CSS_SELECTOR, '.notify-module-error-17z7Pp')
        assert element.is_displayed()

    @pytest.mark.parametrize(['email', 'password'], [('', 'asasda33333'),
                                                     ('12312414a', ''),
                                                     ('', '')])
    def test_negative_auth_empty_input(self, browser, email, password):
        auth(browser, email=email, password=password)
        browser.find_element(By.CSS_SELECTOR, '.authForm-module-disabled-104QGH')
