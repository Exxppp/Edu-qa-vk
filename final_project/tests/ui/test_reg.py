import allure
import pytest

from tests.ui.base import BaseCase


@allure.epic('UI тесты')
@allure.feature('Регистрация')
@pytest.mark.UI
class TestReg(BaseCase):

    def register_user(self, name=None, surname=None, middlename=None, username=None, email=None, password=None,
                      repeat_password=None, checkbox=True):
        user_data = self.builder.user()
        name = name if name is not None else user_data.name
        surname = surname if surname is not None else user_data.surname
        middlename = middlename if middlename is not None else user_data.middle_name
        username = username if username is not None else user_data.username
        email = email if email is not None else user_data.email
        password = password if password is not None else user_data.password
        repeat_password = repeat_password if repeat_password is not None else password
        checkbox = checkbox
        self.register_page.register(name=name, surname=surname, middlename=middlename, username=username, email=email,
                                    password=password, repeat_password=repeat_password, checkbox=checkbox)

    @allure.story('Проверка регистрации и заполнения бд')
    def test_reg_correct_user(self):
        ud = self.builder.user()
        self.register_user(ud.name, ud.surname, ud.middle_name, ud.username, ud.email, ud.password)

        assert self.driver.current_url == self.main_page.url

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

    @allure.story('Проверка регистрации и дополнительного заполнения бд')
    def test_reg_correct_user(self):
        ud = self.builder.user()
        self.register_user(ud.name, ud.surname, ud.middle_name, ud.username, ud.email, ud.password)
        with allure.step('Проверка внесения дополнительных данных в базу'):
            bd_user = self.mysql.get_all_fields_by_username(ud.username)
            with allure.step('Проверка access'):
                assert bd_user.access == 1
            with allure.step('Проверка active'):
                assert bd_user.active == 1
            with allure.step('Проверка start_active_time'):
                assert bd_user.start_active_time

    @allure.story('Проверка регистрации с пустыми полями')
    def test_reg_user_with_empty_fields(self):
        self.register_user('', '', '', '', '', '', '')

        assert self.driver.current_url != self.main_page.url

    @allure.story('Проверка регистрации с пустым полем')
    def test_reg_user_with_empty_field_middlename(self):
        self.register_user(middlename='')

        assert self.driver.current_url == self.main_page.url

    @allure.story('Проверка регистрации с пустым полем')
    def test_reg_user_with_empty_field_name(self):
        name = ''
        self.register_user(name=name)

        assert self.driver.current_url != self.main_page.url

    @allure.story('Проверка регистрации с пустым полем')
    def test_reg_user_with_empty_field_surname(self):
        surname = ''
        self.register_user(surname=surname)

        assert self.driver.current_url != self.main_page.url

    @allure.story('Проверка регистрации с пустым полем')
    def test_reg_user_with_empty_field_username(self):
        username = ''
        self.register_user(username=username)

        assert self.driver.current_url != self.main_page.url

    @allure.story('Проверка регистрации с пустым полем')
    def test_reg_user_with_empty_field_password(self):
        password = ''
        self.register_user(password=password)

        assert self.driver.current_url != self.main_page.url

    @allure.story('Проверка регистрации с пустым полем')
    def test_reg_user_with_empty_field_email(self):
        email = ''
        self.register_user(email=email)

        assert self.driver.current_url != self.main_page.url

    @allure.story('Проверка username по длине')
    @pytest.mark.parametrize('size', [5, 6, 7, 15, 16, 17])
    def test_reg_user_by_username_size(self, size):
        username = self.builder.user(username_length=size).username
        self.register_user(username=username)

        if size == 5:
            assert self.driver.current_url != self.main_page.url
        else:
            assert self.driver.current_url == self.main_page.url

    @allure.story('Проверки некорректного email')
    def test_reg_user_with_incorrect_email(self):
        with allure.step('Точка слева'):
            email = '.' + self.builder.user().email
            self.register_user(email=email)
            assert self.driver.current_url != self.main_page.url
        with allure.step('Точка справа'):
            email = self.builder.user().email + '.'
            self.register_user(email=email)
            assert self.driver.current_url != self.main_page.url
        with allure.step('Пробел слева'):
            email = ' ' + self.builder.user().email
            self.register_user(email=email)
            assert self.driver.current_url != self.main_page.url
        with allure.step('Пробел справа'):
            email = self.builder.user().email + ' '
            self.register_user(email=email)
            assert self.driver.current_url != self.main_page.url
        with allure.step('Без @'):
            email = self.builder.user().email.replace('@', '')
            self.register_user(email=email)
            assert self.driver.current_url != self.main_page.url
        with allure.step('Без точки в домене'):
            email = self.builder.user().email.replace('.', '')
            self.register_user(email=email)
            assert self.driver.current_url != self.main_page.url

    @allure.story('Проверка регистрации без checkbox')
    def test_reg_user_with_empty_field_email(self):
        self.register_user(checkbox=False)

        assert self.driver.current_url != self.main_page.url
