import pytest
from api.client import ApiClient


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://target-sandbox.my.com/')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    return {
        'url': url
    }


@pytest.fixture(scope='session')
def api_client(config):
    return ApiClient(base_url=config['url'], login='testgdhdhsjsjs@gmail.com', password='123456q')
