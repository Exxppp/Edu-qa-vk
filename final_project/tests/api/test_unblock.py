import pytest
import allure
from tests.api.base import BaseCaseApi


@allure.epic('API тесты')
@allure.feature('Разблокировка')
@pytest.mark.API
class TestUnblockApi(BaseCaseApi):

    def test_unblocked_user(self):
        user_data = self.builder.user()
        self.mysql.add_user(user_data.data)
        block_user = self.api_client.block_user(user_data.username)

        assert block_user.status_code == 200

        self.api_client.unblock_user(user_data.username)

        with allure.step('Проверка изменение access пользователя'):
            assert self.mysql.get_all_fields_by_username(user_data.username).access == 1
