from ui.locators.basic_locators import DashboardPageLocators
from ui.pages.base_page import BasePage
from random_content.methods import random_text
import allure


class DashboardPage(BasePage):

    locators = DashboardPageLocators
    url = 'https://target-sandbox.my.com/dashboard'

    @allure.step
    def creating_advertising_campaign_vk_products(self, file_path):
        self.click(self.locators.CREATE_NEW_COMPANY)
        self.click(self.locators.VK_PRODUCTS)
        self.input_text(self.locators.LINK, 'https://www.youtube.com/watch?v=NkmsQnrULLM&ab_channel=MikhailVolkov')
        self.click(self.locators.FIRST_AD_PRODUCT)
        self.input_text(self.locators.NAME_COMPANY, random_text())
        self.upload_file(self.locators.UPLOAD_CREATIVE, file_path)
        self.input_text(self.locators.TITLE_AD, random_text(20))
        self.input_text(self.locators.TEXT_AD, random_text(60))
        self.click(self.locators.SAVE_AD)
        self.click(self.locators.SAVE_COMPANY)
        return self.get_text(self.locators.GET_NAME_COMPANY)

    @allure.step
    def delete_company(self):
        self.click(self.locators.SELECT_COMPANY)
        self.click(self.locators.ACTIONS)
        self.click(self.locators.DELETE)
        self.driver.refresh()
        return self.is_not_element_present(self.locators.GET_NAME_COMPANY, 5)

