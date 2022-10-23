from ..locators.locators import DashboardPageLocators
from .base_page import BasePage


class DashboardPage(BasePage):
    locators = DashboardPageLocators
    url = 'https://target-sandbox.my.com/dashboard'

    def creating_advertising_campaign_vk_products(self, file_path, name_company='my company', title_ad='test',
                                                  text_ad='test'):
        self.click(self.locators.CREATE_NEW_COMPANY)
        self.click(self.locators.VK_PRODUCTS)
        self.input_text(self.locators.LINK, 'https://www.youtube.com/watch?v=NkmsQnrULLM&ab_channel=MikhailVolkov')
        self.click(self.locators.FIRST_AD_PRODUCT)
        self.input_text(self.locators.NAME_COMPANY, name_company)
        self.upload_file(self.locators.UPLOAD_CREATIVE, file_path)
        self.input_text(self.locators.TITLE_AD, title_ad)
        self.input_text(self.locators.TEXT_AD, text_ad)
        self.click(self.locators.SAVE_AD)
        self.click(self.locators.SAVE_COMPANY)
        elem = self.get_text(self.locators.GET_NAME_COMPANY)
        self.click(self.locators.SELECT_ALL_COMPANY)
        self.click(self.locators.ACTIONS)
        self.click(self.locators.DELETE)
        return elem
