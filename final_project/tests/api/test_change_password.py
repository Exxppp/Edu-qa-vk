import pytest
import allure
from tests.api.base import BaseCaseApi
from utils.func import generate_str


@allure.epic('API тесты')
@allure.feature('Смена пароля')
@pytest.mark.API
class TestChangePassApi(BaseCaseApi):

    @allure.story('Проверка статус кода')
    def test_unblocked_user(self):
        user_data = self.builder.user()
        self.mysql.add_user(user_data.data)
        password_new = generate_str()
        change_password = self.api_client.change_password(user_data.username, password_new)

        assert change_password.status_code == 200

    @allure.story('Проверка изменений в бд')
    def test_unblocked_user_change_in_bd(self):
        user_data = self.builder.user()
        self.mysql.add_user(user_data.data)
        password_new = generate_str()
        self.api_client.change_password(user_data.username, password_new)

        with allure.step('Проверка изменнёного пароля'):
            password = self.mysql.get_all_fields_by_username(username=user_data.username).password
            assert password == password_new
