from api.api_base import ApiBase
from builder import Builder
import allure


class ApiClient(ApiBase):

    def create_user_reg(self):
        location = 'reg'
        data = Builder.user().data_reg
        user = self._request('POST', location, data=data)

        return user

    def post_login(self, username, password):
        location = '/login'
        data = {'username': username, 'password': password, 'submit': 'Login'}
        self._request('POST', location, data=data)

    @allure.step('Регистрация пользователя')
    def create_user(self, data=None):
        location = '/api/user'
        if data is None:
            data = Builder.user().data
        user = self._request('POST', location, json=data)

        return user

    @allure.step('Удаление пользователя')
    def delete_user(self, username):
        location = f'/api/user/{username}'
        delete = self._request('DELETE', location)

        return delete

    @allure.step('Смена пароля пользователя')
    def change_password(self, username, new_password):
        location = f'/api/user/{username}/change-password'
        data = {'password': new_password}
        password = self._request('PUT', location, json=data)

        return password

    @allure.step('Блокировка пользователя')
    def block_user(self, username):
        location = f'/api/user/{username}/block'
        block = self._request('POST', location)

        return block

    @allure.step('Разблокировка пользователя')
    def unblock_user(self, username):
        location = f'/api/user/{username}/accept'
        unblock = self._request('POST', location)

        return unblock

    def get_status_app(self):
        location = f'/status'
        status = self._request('GET', location)

        return status
