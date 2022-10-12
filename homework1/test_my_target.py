import pytest
from ui.locators import basic_locators
from base import BaseCase


@pytest.mark.UI
class TestUi(BaseCase):
    def test_login(self):
        self.auth()
        element = self.find(*basic_locators.HTML)
        assert element.get_attribute('data-ga-username') == 'testgdhdhsjsjs@gmail.com'

    def test_edit_contact_information(self):
        self.auth()
        self.browser.get('https://target-sandbox.my.com/profile/contacts')
        self.input_text('Kostya Ivanov Sergeevich', basic_locators.EDIT_INF_INPUT_1)
        self.input_text('241421414121', basic_locators.EDIT_INF_INPUT_2)
        self.input_text('+79193213111', basic_locators.EDIT_INF_INPUT_3)
        self.click(basic_locators.EDIT_INF_BUTTON)
        assert self.wait(basic_locators.EDIT_INF_SUCCESS, method='is_displayed')

    @pytest.mark.parametrize(['numbers_elements', 'selector'], [(0, basic_locators.DASHBOARD),
                                                                (1, basic_locators.SEGMENTS),
                                                                (2, basic_locators.BILLING),
                                                                (3, basic_locators.STATISTICS),
                                                                (4, basic_locators.PRO),
                                                                (5, basic_locators.PROFILE),
                                                                (6, basic_locators.TOOLS),
                                                                (7, basic_locators.HELP)])
    def test_elements_on_headers(self, browser, numbers_elements, selector):
        self.auth()
        self.wait(basic_locators.ELEMENTS_ON_HEADERS, method='len')
        self.click_in_array(basic_locators.ELEMENTS_ON_HEADERS, numbers_elements)
        if numbers_elements == 7:
            self.browser.switch_to.window(browser.window_handles[1])
        assert self.wait(selector, method='is_displayed')

    def test_logout(self):
        self.auth()
        self.logout()
        element = self.find(*basic_locators.HTML)
        assert element.get_attribute('data-ga-userid') == ''

    @pytest.mark.parametrize(['email', 'password'], [('testgd hdhsjsj', 'asasda33333'),
                                                     ('12312414a', 'sadsadsad')])
    def test_negative_auth(self, browser, email, password):
        self.auth(email, password)
        assert self.wait(basic_locators.NOTIFY_AUTH_FORM, method='is_displayed')

    @pytest.mark.parametrize(['email', 'password'], [('', 'asasda33333'),
                                                     ('12312414a', ''),
                                                     ('', '')])
    def test_negative_auth_empty_input(self, browser, email, password):
        self.auth(email=email, password=password)
        self.find(*basic_locators.DISABLE_BUTTON)

