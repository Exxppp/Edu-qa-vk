import allure

from ui.locators.basic_locators import DashboardPageLocators
from ui.pages.base_page import BasePage
from random_content.methods import generate_random_text


class DashboardPage(BasePage):
    locators = DashboardPageLocators
    url = 'https://target-sandbox.my.com/dashboard'

    @allure.step('create company')
    def creating_advertising_campaign_vk_products(self, file_path):
        self.click(self.locators.CREATE_NEW_COMPANY)
        self.click(self.locators.VK_PRODUCTS)
        self.input_text(self.locators.LINK, 'https://www.youtube.com/watch?v=NkmsQnrULLM&ab_channel=MikhailVolkov')
        self.click(self.locators.AD_PRODUCT_90X75)
        self.scroll_down()
        self.input_text(self.locators.NAME_COMPANY, generate_random_text())
        self.upload_file(self.locators.UPLOAD_CREATIVE, file_path)
        self.input_text(self.locators.TITLE_AD, generate_random_text(20))
        self.input_text(self.locators.TEXT_AD, generate_random_text(40))
        self.click(self.locators.SAVE_COMPANY)

    @allure.step('delete company')
    def delete_company(self):
        self.click(self.locators.SELECT_COMPANY)
        self.click(self.locators.ACTIONS)
        self.click(self.locators.DELETE)
        self.driver.refresh()

    @allure.step('get name company')
    def get_name_company(self):
        self.open()
        return self.get_text(self.locators.GET_NAME_COMPANY)

    @allure.step('count companies')
    def count_companies(self):
        self.open()
        count = self.driver.find_elements(*self.locators.GET_NAME_COMPANY)

        return len(count)
