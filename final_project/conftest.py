import os
import shutil
import subprocess
from copy import copy

from api.client import ApiClient
from builder import Builder
from mysql.client import MysqlClient
from ui.fixtures import *
from utils.func import wait_ready


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='pass', db_name='DB_MYAPP')

    config.repo_root = os.path.abspath(os.path.join(__file__, os.path.pardir))
    base_test_dir = os.path.join(config.repo_root, 'tests_logs')

    if not hasattr(config, 'workerinput'):

        app_stderr_path = os.path.join(config.repo_root, 'tmp', 'app_stderr')
        app_stdout_path = os.path.join(config.repo_root, 'tmp', 'app_stdout')
        os.makedirs(os.path.dirname(app_stderr_path), exist_ok=True)
        app_stderr = open(app_stderr_path, 'w')
        app_stdout = open(app_stdout_path, 'w')
        config.app_stderr = app_stderr
        config.app_stdout = app_stdout

        env = copy(os.environ)
        subprocess.run("docker network create selenoid")
        subprocess.Popen("docker compose up", stderr=app_stderr, stdout=app_stdout, env=env)
        wait_ready(host='localhost', port='9090')

        # logs
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

    # add user
    user_data = Builder.user()
    mysql_client.connect()
    mysql_client.add_user(user_data.data)

    config.user_data = user_data
    config.base_test_dir = base_test_dir
    config.mysql_client = mysql_client


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
def api_client():
    return ApiClient()


@pytest.fixture(scope='session')
def cookies_ui(config, api_client: ApiClient, request):
    api_client.post_login(username=request.config.user_data.username, password=request.config.user_data.password)
    cookies = api_client.session.cookies
    name, value = tuple(cookies.get_dict().items())[0]
    return name, value


@pytest.fixture(scope='session')
def cookies_api(config, api_client: ApiClient, request):
    api_client.post_login(username=request.config.user_data.username, password=request.config.user_data.password)
    cookies = api_client.session.cookies
    return cookies


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        env = copy(os.environ)
        app_stderr_path = os.path.join(config.repo_root, 'tmp', 'down_app_stderr')
        app_stdout_path = os.path.join(config.repo_root, 'tmp', 'down_app_stdout')
        down_app_stderr = open(app_stderr_path, 'w')
        down_app_stdout = open(app_stdout_path, 'w')

        down_docker = subprocess.Popen('docker compose down', stderr=down_app_stderr, stdout=down_app_stdout, env=env)
        down_docker.wait(120)

        subprocess.run("docker network rm selenoid")

        down_app_stderr.close()
        down_app_stdout.close()
        config.app_stderr.close()
        config.app_stdout.close()
