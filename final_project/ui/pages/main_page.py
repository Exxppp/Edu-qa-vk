from ui.pages.base_page import BasePage
from ui.locators.basic_locators import MainPageLocators


class MainPage(BasePage):

    locators = MainPageLocators
    url = 'http://localhost:9090/welcome/'
