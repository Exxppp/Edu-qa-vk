import pytest

from builder import Builder
from mysql.client import MysqlClient
from api.client import ApiClient


class BaseCaseApi:

    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, mysql_client):
        self.api_client: ApiClient = api_client
        self.builder = Builder()
        self.mysql: MysqlClient = mysql_client

        if self.authorize:
            user_data = Builder.user()
            mysql_client.add_user(user_data.data)
            api_client.post_login(user_data.username, user_data.password)
            self.auth_user_data = user_data
