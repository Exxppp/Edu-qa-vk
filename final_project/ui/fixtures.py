import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.register_page import RegisterPage


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')
    parser.addoption('--video', action='store_true')
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru, es or other")


@pytest.fixture()
def driver(config, temp_dir, logs=True):
    selenoid = config['selenoid']
    vnc = config['vnc']
    video = config['video']
    language = config['language']
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if logs:
        options.add_experimental_option("prefs", {"download.default_directory": temp_dir})
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '106.0',
            'selenoid:options': {'enableVNC': vnc,
                                 'enableVideo': video}}
        driver = webdriver.Remote(
            command_executor=selenoid,
            options=options,
            desired_capabilities=capabilities
        )
    else:
        if config['headless']:
            options.add_argument('--headless')
            options.add_argument('--window-size=1920x1080')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, url=config['url'])


@pytest.fixture
def login_page(driver, config):
    return LoginPage(driver=driver, url=config['url'] + 'login')


@pytest.fixture
def register_page(driver, config):
    return RegisterPage(driver=driver, url=config['url'] + 'reg')


@pytest.fixture
def main_page(driver, config):
    return MainPage(driver=driver, url=config['url'] + 'welcome/')
