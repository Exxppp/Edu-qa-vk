from ui.locators.locators_android import InfoPageANDROIDLocators
from ui.locators.locators_web import InfoPageLocators
from ui.pages.base_page import BasePage


class InfoPage(BasePage):
    locators = InfoPageLocators

    def get_about_version(self):
        pass

    def get_about_copyright(self):
        pass


class InfoPageANDROID(InfoPage):
    locators = InfoPageANDROIDLocators

    def get_about_version(self):
        return self.get_text(self.locators.VERSION).split(' ')[-1]

    def get_about_copyright(self):
        return self.get_text(self.locators.COPYRIGHT).split('. ')[-1]
