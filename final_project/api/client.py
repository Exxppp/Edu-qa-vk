from api.api_base import ApiBase
from builder import Builder


class ApiClient(ApiBase):

    def create_user(self):
        location = '/api/user'
        data = Builder.user().data
        user = self._request('POST', location, json=data)

        return user

    def create_user_reg(self):
        location = 'reg'
        data = Builder.user().data_reg
        user = self._request('POST', location, data=data)

        return user

    def change_password(self, username, new_password):
        location = f'/api/user/{username}'
        data = {'password': new_password}
        password = self._request('PUT', location, data=data)

        return password


