from ui.locators.locators_android import MainPageANDROIDLocators
from ui.locators.locators_web import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def open_keyboard(self):
        pass

    def send_expression(self, expression):
        pass

    def send_keys_news(self):
        pass

    def get_answer(self):
        pass

    def send_text_russia(self):
        pass

    def get_name_country(self):
        pass

    def get_description_country(self):
        pass

    def population_of_russia(self):
        pass

    def get_population_of_russia(self):
        pass

    def go_to_settings(self):
        pass

    def get_name_news_source(self):
        pass


class MainPageANDROID(MainPage):
    locators = MainPageANDROIDLocators()

    def open_keyboard(self):
        self.click_for_android(self.locators.KEYBOARD)

    def send_keys(self, text):
        self.input_text(self.locators.INPUT_TEXT, text)
        self.click_for_android(self.locators.SEND_TEXT)

    def send_expression(self, expression):
        self.send_keys(expression)

    def send_keys_news(self):
        self.send_keys('News')

    def send_text_russia(self):
        self.send_keys('Russia')
        self.driver.hide_keyboard()

    def get_answer(self):
        return self.get_text(self.locators.EXPRESSION_RESULT)

    def get_name_country(self):
        return self.get_text(self.locators.GET_TITLE)

    def get_description_country(self):
        return self.get_text(self.locators.GET_DESCRIPTION_COUNTRY)[:24]

    def population_of_russia(self):
        el = self.search_element_by_text_use_scroll_left(self.locators.SEARCH_EL_IN_DOWN_PANEL, 'население россии')
        el.click()
        # self.click_for_android(self.locators.POPULATION_OF_RUSSIA)

    def get_population_of_russia(self):
        return self.get_text(self.locators.GET_TITLE)

    def get_name_news_source(self):
        return self.get_text(self.locators.PLAYER_NAME)

    def go_to_settings(self):
        self.click_for_android(self.locators.SETTINGS)
