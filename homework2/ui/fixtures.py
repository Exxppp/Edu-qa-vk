import os
import shutil
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.dashboard_page import DashboardPage
from .pages.segments_page import SegmentsPage


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if not hasattr(config, 'workerunput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_temp_dir = base_dir


@pytest.fixture()
def driver(config, temp_dir):
    selenoid = config['selenoid']
    vnc = config['vnc']
    video = config['video']
    language = config['language']
    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": temp_dir})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '106.0',
            'selenoid:options': {'enableVNC': vnc,
                                 'enableVideo': video}}
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    else:
        if config['headless']:
            options.add_argument('--headless')
            options.add_argument('--window-size=1920x1080')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver=driver)


@pytest.fixture
def segments_page(driver):
    return SegmentsPage(driver=driver)
