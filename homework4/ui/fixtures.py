import os

import allure
import pytest
from appium import webdriver
from ui import pages
from ui.capability import capability_select
from ui.pages.base_page import BasePage


class UnsupportedBrowserType(Exception):
    pass


def get_page(device, page_class):
    if device == 'android':
        page_class += 'ANDROID'
    page = getattr(pages, page_class, None)
    if page is None:
        raise Exception(f'No such page {page_class}')
    return page


def get_driver(device_os, appium_url, file):
    if device_os == 'android':
        desired_caps = capability_select(device_os, file)
        driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
        return driver
    else:
        raise UnsupportedBrowserType(f' Unsupported device_os type {device_os}')


@pytest.fixture(scope='function')
def driver(config, test_dir, file_path):
    device_os = config['device_os']
    appium_url = config['appium']
    browser = get_driver(device_os, appium_url, file=file_path)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def permission_page(driver, config):
    page = get_page(config['device_os'], 'PermissionPage')
    return page(driver=driver, config=config)


@pytest.fixture
def main_page(driver, config):
    page = get_page(config['device_os'], 'MainPage')
    return page(driver=driver, config=config)


@pytest.fixture
def settings_page(driver, config):
    page = get_page(config['device_os'], 'SettingsPage')
    return page(driver=driver, config=config)


@pytest.fixture
def info_page(driver, config):
    page = get_page(config['device_os'], 'InfoPage')
    return page(driver=driver, config=config)


@pytest.fixture
def news_source_page(driver, config):
    page = get_page(config['device_os'], 'NewsSourcePage')
    return page(driver=driver, config=config)


@pytest.fixture(scope='function')
def ui_report(driver, request, test_dir, config):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)
