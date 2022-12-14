from ui.pages.base_page import BasePage
from ui.locators.basic_locators import MainPageLocators
import allure


class MainPage(BasePage):

    locators = MainPageLocators

    @allure.step('Нажимаем на кнопку HOME')
    def go_to_home(self):
        self.click(self.locators.HOME)

    @allure.step('Нажимаем на кнопку PYTHON')
    def go_to_python(self):
        self.click(self.locators.PYTHON)

    @allure.step('Нажимаем на кнопку PYTHON_HISTORY')
    def go_to_python_history(self):
        self.move_and_click_to_next_element(self.locators.PYTHON, self.locators.PYTHON_HISTORY)

    @allure.step('Нажимаем на кнопку ABOUT_FLASK')
    def go_to_about_flask(self):
        self.move_and_click_to_next_element(self.locators.PYTHON, self.locators.ABOUT_FLASK)

    @allure.step('Нажимаем на кнопку CENTOS_DOWNLOAD')
    def go_to_download_centos(self):
        self.move_and_click_to_next_element(self.locators.LINUX, self.locators.CENTOS_DOWNLOAD)

    @allure.step('Нажимаем на кнопку WIRESHARK_NEWS')
    def go_to_wireshark_news(self):
        self.move_and_click_to_next_element(self.locators.NETWORK, self.locators.WIRESHARK_NEWS)

    @allure.step('Нажимаем на кнопку WIRESHARK_DOWNLOAD')
    def go_to_wireshark_download(self):
        self.move_and_click_to_next_element(self.locators.NETWORK, self.locators.WIRESHARK_DOWNLOAD)

    @allure.step('Нажимаем на кнопку TCPDUMP_EXAMPLES')
    def go_to_tcpdump_examples(self):
        self.move_and_click_to_next_element(self.locators.NETWORK, self.locators.TCPDUMP_EXAMPLES)

    @allure.step('Нажимаем на кнопку WHAT_IS_AN_API')
    def go_to_what_is_an_api(self):
        self.click(self.locators.WHAT_IS_AN_API)

    @allure.step('Нажимаем на кнопку FUTURE_OF_INTERNET')
    def go_to_future_of_internet(self):
        self.click(self.locators.FUTURE_OF_INTERNET)

    @allure.step('Нажимаем на кнопку SMTP')
    def go_to_smtp(self):
        self.click(self.locators.SMTP)

    @allure.step('Получаем текст username')
    def get_text_username(self):
        text = self.get_text(self.locators.USERNAME_INFO)
        return text

    @allure.step('Получаем текст fio')
    def get_text_fio(self):
        text = self.get_text(self.locators.NAMES_INFO)
        return text

    @allure.step('Получаем текст vk id')
    def get_text_vk_id(self):
        return self.get_text(self.locators.VK_ID_INFO)

    @allure.step('Разлогиниваемся')
    def logout(self):
        self.click(self.locators.LOGOUT)
