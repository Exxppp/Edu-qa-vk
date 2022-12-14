import allure
import pytest

from tests.ui.base import BaseCase
from static.main_page.links import *


@allure.epic('UI тесты')
@allure.feature('Главная страница')
@pytest.mark.UI
class TestMainPage(BaseCase):
    authorize = True

    @allure.story('Проверки переходов')
    def test_button_home(self):
        self.main_page.go_to_home()

        assert self.driver.current_url == self.driver.current_url, 'Не та ссылка'

    @allure.story('Проверки переходов')
    def test_button_python(self):
        current_window = self.driver.current_window_handle
        self.main_page.go_to_python()
        with self.switch_to_window(current_window):
            assert self.driver.current_url == PYTHON, 'Не та ссылка'
        assert len(self.driver.window_handles) == 2, 'Не открывается новая вкладка'

    @allure.story('Проверки переходов')
    def test_button_python_history(self):
        current_window = self.driver.current_window_handle
        self.main_page.go_to_python()
        with self.switch_to_window(current_window):
            assert self.driver.current_url == PYTHON, 'Не та ссылка'
        assert len(self.driver.window_handles) == 2, 'Не открывается новая вкладка'

    @allure.story('Проверки переходов')
    def test_button_about_flask(self):
        current_window = self.driver.current_window_handle
        self.main_page.go_to_about_flask()
        with self.switch_to_window(current_window):
            assert self.driver.current_url == ABOUT_FLASK, 'Не та ссылка'
        assert len(self.driver.window_handles) == 2, 'Не открывается новая вкладка'

    @allure.story('Проверки переходов')
    def test_button_download_centos(self):
        current_window = self.driver.current_window_handle
        self.main_page.go_to_download_centos()
        with self.switch_to_window(current_window):
            assert self.driver.current_url == LINUX_DOWNLOAD_CENTOS, 'Не та ссылка'
        assert len(self.driver.window_handles) == 2, 'Не открывается новая вкладка'

    @allure.story('Проверки переходов')
    def test_button_wireshark_news(self):
        current_window = self.driver.current_window_handle
        self.main_page.go_to_wireshark_news()
        with self.switch_to_window(current_window):
            assert self.driver.current_url == WIRESHARK_NEWS, 'Не та ссылка'
        assert len(self.driver.window_handles) == 2, 'Не открывается новая вкладка'

    @allure.story('Проверки переходов')
    def test_button_wireshark_download(self):
        current_window = self.driver.current_window_handle
        self.main_page.go_to_wireshark_download()
        with self.switch_to_window(current_window):
            assert self.driver.current_url == WIRESHARK_DOWNLOAD, 'Не та ссылка'
        assert len(self.driver.window_handles) == 2, 'Не открывается новая вкладка'

    @allure.story('Проверки переходов')
    def test_button_tcpdump(self):
        current_window = self.driver.current_window_handle
        self.main_page.go_to_tcpdump_examples()
        with self.switch_to_window(current_window):
            assert self.driver.current_url == TCP_DUMP_EXAMPLES, 'Не та ссылка'
        assert len(self.driver.window_handles) == 2, 'Не открывается новая вкладка'

    @allure.story('Проверки переходов')
    def test_button_what_is_api(self):
        current_window = self.driver.current_window_handle
        self.main_page.go_to_what_is_an_api()
        with self.switch_to_window(current_window):
            assert self.driver.current_url == WHAT_IS_AN_API, 'Не та ссылка'
        assert len(self.driver.window_handles) == 2, 'Не открывается новая вкладка'

    @allure.story('Проверки переходов')
    def test_button_future_of_internet(self):
        current_window = self.driver.current_window_handle
        self.main_page.go_to_future_of_internet()
        with self.switch_to_window(current_window):
            assert self.driver.current_url == FUTURE_OF_INTERNET, 'Не та ссылка'
        assert len(self.driver.window_handles) == 2, 'Не открывается новая вкладка'

    @allure.story('Проверки переходов')
    def test_button_smtp(self):
        current_window = self.driver.current_window_handle
        self.main_page.go_to_smtp()
        with self.switch_to_window(current_window):
            assert self.driver.current_url == SMTP, 'Не та ссылка'
        assert len(self.driver.window_handles) == 2, 'Не открывается новая вкладка'

    @allure.story('Проверка отображения пользовательской иноформации')
    def test_display_user_info(self):
        assert self.main_page.get_text_username() == f'Logged as {self.auth_user_data.username}'
        assert self.main_page.get_text_fio() == f'User: {self.auth_user_data.name} {self.auth_user_data.surname} ' \
                                                f'{self.auth_user_data.middle_name}'
        assert self.main_page.get_text_vk_id()

    @allure.story('Проверка logout')
    def test_logout_button(self):
        current_url = self.driver.current_url
        self.main_page.logout()

        assert current_url != self.driver.current_url, 'Кнопка logout не работает'

        self.driver.get(self.main_page.url)

        assert self.driver.current_url != self.main_page.url, 'Пользователь не разлогился'
