import os
import shutil
from ui.fixtures import *
from mysql.client import MysqlClient
from api.client import ApiClient


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='pass', db_name='DB_MYAPP')

    if not hasattr(config, 'workerinput'):
        # logs
        config.repo_root = os.path.abspath(os.path.join(__file__, os.path.pardir))

        base_test_dir = os.path.join(config.repo_root, 'tests_logs')
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

        config.base_test_dir = base_test_dir

        # clear table
        mysql_client.clear_table()

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
def api_client(config):
    return ApiClient(base_url=config['url'])
