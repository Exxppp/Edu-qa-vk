from ui.locators.locators_android import NewsSourcePageANDROIDLocators
from ui.locators.locators_web import NewsSourcePageLocators
from ui.pages.base_page import BasePage


class NewsSourcePage(BasePage):
    locators = NewsSourcePageLocators

    def add_mail_ru_to_news_source(self):
        pass

    def go_to_settings_page(self):
        pass


class NewsSourcePageANDROID(NewsSourcePage):
    locators = NewsSourcePageANDROIDLocators

    def add_mail_ru_to_news_source(self):
        self.click_for_android(self.locators.MAIL_RU)

        assert self.find(self.locators.MAIL_RU_SELECTED)

    def go_to_settings_page(self):
        self.click_for_android(self.locators.BACK_BUTTON)
