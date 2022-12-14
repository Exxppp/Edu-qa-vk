import pytest
import allure
from utils.func import generate_str

from tests.ui.base import BaseCase


@allure.epic('UI тесты')
@allure.feature('Авторизация')
@pytest.mark.UI
class TestLogin(BaseCase):

    @allure.story('Проверка авторизации')
    def test_login(self):
        user_data = self.builder.user()
        self.mysql.add_user(user_data.data)
        self.login_page.login(user_data.username, user_data.password)

        assert self.driver.current_url == self.main_page.url

    @allure.story('Проверка авторизации с пустыми полями')
    def test_login__with_empty_fields(self):
        self.login_page.login('', '')

        assert self.driver.current_url != self.main_page.url

    @allure.story('Проверка авторизации с пустым паролем')
    def test_login_with_empty_field_password(self):
        user_data = self.builder.user()
        self.mysql.add_user(user_data.data)
        self.login_page.login(user_data.username, '')

        assert self.driver.current_url != self.main_page.url

    @allure.story('Проверка авторизации с некорректным паролем')
    def test_login_with_incorrect_password(self):
        user_data = self.builder.user()
        incorrect_password = generate_str(25)
        self.mysql.add_user(user_data.data)
        self.login_page.login(user_data.username, incorrect_password)

        assert self.driver.current_url != self.main_page.url
        assert self.login_page.get_text_from_alert()

    @allure.story('Проверка авторизации заблокированного пользователя')
    def test_login_blocked_user(self):
        user_data = self.builder.user()
        self.mysql.add_user(user_data.data)
        self.mysql.set_user_access(user_data.username, access_status=0)
        self.login_page.login(user_data.username, user_data.password)

        assert self.driver.current_url != self.main_page.url
