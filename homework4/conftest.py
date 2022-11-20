import logging
import shutil
import sys

from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--os', default='android')
    parser.addoption('--appium', default='http://127.0.0.1:4723/wd/hub')
    parser.addoption('--debug_log', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    device_os = request.config.getoption('--os')
    appium = request.config.getoption('--appium')
    debug_log = request.config.getoption('--debug_log')
    return {'device_os': device_os, 'debug_log': debug_log, 'appium': appium}


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))


@pytest.fixture(scope='session')
def file_path(repo_root):
    return os.path.join(repo_root, 'apk', 'marussia_1.70.0.apk')


@pytest.fixture()
def get_version_apk(repo_root):
    version = os.listdir(os.path.join(repo_root, 'apk'))[0].replace('marussia_', '').replace('.apk', '')
    return version


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "skip_platform: skip test for necessary platform ",
    )

    if sys.platform.startswith('win'):
        base_test_dir = 'C:\\tests'
    else:
        base_test_dir = '/tmp/tests'
    if os.path.exists(base_test_dir):
        shutil.rmtree(base_test_dir)

    config.base_test_dir = base_test_dir


@pytest.fixture(scope='function')
def test_dir(request):
    test_dir = os.path.join(request.config.base_test_dir, request._pyfuncitem.nodeid)
    test_dir = os.path.abspath(test_dir).replace('::', '_')
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='function')
def logger(test_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(test_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


@pytest.fixture(scope='session', autouse=True)
def add_allure_environment_property(request, config):
    """
    В зависимости от типа девайса добавляем в наши environment аллюра
    environment.properties должен лежать внутри директории файлов allure в виде словаря
    """
    alluredir = request.config.getoption('--alluredir')
    if alluredir:
        env_props = dict()
        if config['device_os'] == 'android':
            env_props['Appium'] = '1.20'
            env_props['Android_emulator'] = '11.0'

        if not os.path.exists(alluredir):
            os.makedirs(alluredir)

        allure_env_path = os.path.join(alluredir, 'environment.properties')

        with open(allure_env_path, 'w') as f:
            for key, value in list(env_props.items()):
                f.write(f'{key}={value}\n')
