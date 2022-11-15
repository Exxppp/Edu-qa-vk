import os

import pytest

from api.client import ApiClient


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def userdata_path(repo_root):
    return os.path.join(repo_root, 'files', 'userdata.txt')


@pytest.fixture(scope='session')
def api_client(credentials):
    return ApiClient(login=credentials[0], password=credentials[1])


@pytest.fixture(scope='session')
def credentials(userdata_path):
    with open(userdata_path, 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()

    return user, password
