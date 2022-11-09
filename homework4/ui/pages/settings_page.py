from ui.locators.locators_android import SettingsPageANDROIDLocators
from ui.locators.locators_web import SettingsPageLocators
from ui.pages.base_page import BasePage


class SettingsPage(BasePage):
    locators = SettingsPageLocators()

    def go_to_news_source_page(self):
        pass

    def go_to_main_page(self):
        pass

    def go_to_info_page(self):
        pass


class SettingsPageANDROID(SettingsPage):
    locators = SettingsPageANDROIDLocators

    def go_to_news_source_page(self):
        self.swipe_to_element(self.locators.NEWS_SOURCE, 2)
        self.click_for_android(self.locators.NEWS_SOURCE)

    def go_to_main_page(self):
        self.click_for_android(self.locators.CLOSE_SETTINGS)

    def go_to_info_page(self):
        self.swipe_to_element(self.locators.NEWS_SOURCE, 3)
        self.click_for_android(self.locators.ABOUT)
