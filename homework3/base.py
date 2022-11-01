import pytest
from builder import Builder


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        self.builder = Builder

    @pytest.fixture(scope='session', autouse=True)
    def login(self, api_client):
        if self.authorize:
            api_client.post_login()
