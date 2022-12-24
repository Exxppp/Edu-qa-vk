import http.client
import logging
import os
import shutil
import subprocess
import sys
import time
from copy import copy

import pytest
import requests

import settings
from client.api_client import ApiClient

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))
repo_root_2 = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
if sys.platform.startswith('win'):
    venv_dir = 'Scripts'
    python_name = 'python'
    exit_code = 1
else:
    venv_dir = 'bin'
    python_name = 'python3.10'
    exit_code = -15
python_path = os.path.join(repo_root_2, 'venv', venv_dir, python_name)


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except requests.exceptions.ConnectionError:
            pass

    if not started:
        raise RuntimeError('App did not started in 5s!')


def pytest_configure(config):
    base_test_dir = os.path.join(repo_root, 'tests_logs')

    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

    config.base_test_dir = base_test_dir

    if not hasattr(config, 'workerinput'):
        ######### app configuration #########

        app_path = os.path.join(repo_root, 'application', 'app.py')

        env = copy(os.environ)
        env.update({'APP_HOST': settings.APP_HOST, 'APP_PORT': settings.APP_PORT})
        env.update({'MOCK_HOST': settings.MOCK_HOST, 'MOCK_PORT': settings.MOCK_PORT})

        app_stderr_path = os.path.join(repo_root, 'tmp', 'app_stderr')
        app_stdout_path = os.path.join(repo_root, 'tmp', 'app_stdout')
        app_stderr = open(app_stderr_path, 'w')
        app_stdout = open(app_stdout_path, 'w')

        app_proc = subprocess.Popen([python_path, app_path], stderr=app_stderr, stdout=app_stdout, env=env)
        config.app_proc = app_proc
        config.app_stderr = app_stderr
        config.app_stdout = app_stdout
        wait_ready(settings.APP_HOST, settings.APP_PORT)

        ######### mock configuration #########

        mock_path = os.path.join(repo_root, 'mock', 'flask_mock.py')

        mock_stderr_path = os.path.join(repo_root, 'tmp', 'mock_stderr')
        mock_stdout_path = os.path.join(repo_root, 'tmp', 'mock_stdout')
        mock_stderr = open(mock_stderr_path, 'w')
        mock_stdout = open(mock_stdout_path, 'w')

        mock_proc = subprocess.Popen([python_path, mock_path], stderr=mock_stderr, stdout=mock_stdout, env=env)
        config.mock_proc = mock_proc
        config.mock_stderr = mock_stderr
        config.mock_stdout = mock_stdout
        wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_test_dir, request._pyfuncitem.nodeid)
    test_dir = os.path.abspath(test_dir).replace('::', '_')
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def api_client():
    return ApiClient()


@pytest.fixture(scope='function', autouse=True)
def logger(temp_dir):
    log = logging.getLogger(__name__)
    http.client.HTTPConnection.debuglevel = 1

    def print_to_log(*args):
        log.debug(' '.join(args))
    http.client.print = print_to_log

    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.DEBUG

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setLevel(log_level)

    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


def pytest_unconfigure(config):
    config.app_proc.terminate()
    exit_code_app = config.app_proc.wait()

    config.app_stderr.close()
    config.app_stdout.close()

    config.mock_proc.terminate()
    exit_code_mock = config.mock_proc.wait()

    config.mock_stderr.close()
    config.mock_stdout.close()

    assert exit_code_app == exit_code
    assert exit_code_mock == exit_code
