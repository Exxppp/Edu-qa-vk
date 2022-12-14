import pytest
import allure
from tests.api.base import BaseCaseApi


@allure.epic('API тесты')
@allure.feature('Удаление')
@pytest.mark.API
class TestDeleteApi(BaseCaseApi):

    def test_delete_user(self):
        user_data = self.builder.user()
        self.api_client.create_user(user_data.data)
        delete = self.api_client.delete_user(username=user_data.username)

        with allure.step('Проверка статус кода'):
            assert delete.status_code == 204

        with allure.step('Проверка удалён ли пользователь в базе'):
            user = self.mysql.get_all_fields_by_username(user_data.username)
            assert user is None
