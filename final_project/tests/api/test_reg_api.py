import pytest
import allure
from base import BaseCaseApi

STATUS_CODE_CREATE = 210


@allure.epic('API тесты')
@allure.feature('Регистрация')
@pytest.mark.API
class TestRegApi(BaseCaseApi):

    @allure.story('Регистрация пользователя')
    def test_reg_user(self):
        user = self.api_client.create_user()

        assert user.status_code == 201

    @allure.story('Регистрация пользователя, с только пробельными символами')
    def test_reg_user_with_empty_field_name(self):
        user_data = self.builder.user(name='  ')
        user = self.api_client.create_user(user_data.data)

        assert user.status_code != STATUS_CODE_CREATE

    @allure.story('Регистрация пользователя, с только пробельными символами')
    def test_reg_user_with_empty_field_surname(self):
        user_data = self.builder.user(surname='  ')
        user = self.api_client.create_user(user_data.data)

        assert user.status_code != STATUS_CODE_CREATE

    @allure.story('Регистрация пользователя, с только пробельными символами')
    def test_reg_user_with_empty_field_miidle_name(self):
        user_data = self.builder.user(middle_name='    ')
        user = self.api_client.create_user(user_data.data)

        assert user.status_code != STATUS_CODE_CREATE

    @allure.story('Регистрация пользователя, с только пробельными символами')
    def test_reg_user_with_empty_field_username(self):
        user_data = self.builder.user(username='          ')
        user = self.api_client.create_user(user_data.data)

        assert user.status_code != STATUS_CODE_CREATE

    @allure.story('Регистрация пользователя, с только пробельными символами')
    def test_reg_user_with_empty_field_email(self):
        user_data = self.builder.user(email='           ')
        user = self.api_client.create_user(user_data.data)

        assert user.status_code != STATUS_CODE_CREATE

    @allure.story('Регистрация пользователя, с только пробельными символами')
    def test_reg_user_with_empty_field_password(self):
        user_data = self.builder.user(password='           ')
        user = self.api_client.create_user(user_data.data)

        assert user.status_code != STATUS_CODE_CREATE

    @allure.story('Проверка базы данных')
    def test_reg_user(self):
        ud = self.builder.user()
        self.api_client.create_user(ud.data)

        with allure.step('Проверка внесения данных в базу'):
            bd_user = self.mysql.get_all_fields_by_username(ud.username)
            with allure.step('Проверка имени'):
                assert bd_user.name == ud.name
            with allure.step('Проверка фамилии'):
                assert bd_user.surname == ud.surname
            with allure.step('Проверка email'):
                assert bd_user.email == ud.email
            with allure.step('Проверка пароля'):
                assert bd_user.password == ud.password
            with allure.step('Проверка отчества'):
                assert bd_user.middlename == ud.middle_name

        with allure.step('Проверка внесения дополнительных данных в базу'):
            with allure.step('Проверка access'):
                assert bd_user.access == 1
            with allure.step('Проверка active'):
                assert bd_user.active == 1
            with allure.step('Проверка start_active_time'):
                assert bd_user.start_active_time
