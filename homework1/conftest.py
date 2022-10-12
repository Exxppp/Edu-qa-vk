import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')


@pytest.fixture()
def config(request):
    headless = request.config.getoption('--headless')
    return headless


@pytest.fixture(scope='function')
def browser(config):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if config:
        options.add_argument('--headless')
        options.add_argument('--window-size=1920x1080')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    browser.quit()
