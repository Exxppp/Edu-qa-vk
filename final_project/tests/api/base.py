import pytest

from api.client import ApiClient
from builder import Builder
from mysql.client import MysqlClient


class BaseCaseApi:

    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, mysql_client, request):
        self.api_client: ApiClient = api_client
        self.builder = Builder()
        self.mysql: MysqlClient = mysql_client

        if self.authorize:
            cookies = request.getfixturevalue('cookies_api')
            self.api_client.session.cookies.update(cookies)
            self.auth_user_data = request.config.user_data
