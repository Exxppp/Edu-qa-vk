import os
import shutil
import subprocess
import time

import requests

from ui.fixtures import *
from mysql.client import MysqlClient
from api.client import ApiClient


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='pass', db_name='DB_MYAPP')

    config.repo_root = os.path.abspath(os.path.join(__file__, os.path.pardir))
    base_test_dir = os.path.join(config.repo_root, 'tests_logs')

    if not hasattr(config, 'workerinput'):

        app_stderr = open('tmp/up_stderr', 'w')
        app_stdout = open('tmp/up_stdout', 'w')

        up_docker = subprocess.Popen("docker compose up -d", stderr=app_stderr, stdout=app_stdout)
        wait_ready(host='localhost', port='9090')

        # logs
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

        # clear table
        mysql_client.clear_table()

    config.base_test_dir = base_test_dir

    mysql_client.connect()
    config.mysql_client = mysql_client


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 120:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError('App did not started in 5s!')


@pytest.fixture(scope='session')
def config(request):
    debug_log = request.config.getoption('--debug_log')
    headless = request.config.getoption('--headless')
    video = request.config.getoption('--video')
    language = request.config.getoption('--language')
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
        url = 'http://myapp:9090/'
    else:
        selenoid = None
        vnc = False
        url = 'http://localhost:9090/'

    return {
        'debug_log': debug_log,
        'headless': headless,
        'selenoid': selenoid,
        'vnc': vnc,
        'video': video,
        'language': language,
        'url': url
    }


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_test_dir, request._pyfuncitem.nodeid)
    test_dir = os.path.abspath(test_dir).replace('::', '_')
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()


@pytest.fixture(scope='session')
def api_client(config):
    return ApiClient()
